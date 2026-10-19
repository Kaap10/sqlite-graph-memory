# -*- coding: utf-8 -*-
"""The star line after `sgm-ask --ab`: shown once per machine, never to machines.

Each case checks behaviour that changes if the guard is removed: delete the marker
write and the second call speaks again; drop the CI or env check and those calls
speak too.
"""
import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from sqlite_graph_memory.brain_ask import maybe_star_prompt, STAR_MARKER, STAR_URL  # noqa: E402


def _call(tmp_path, **env):
    buf = io.StringIO()
    shown = maybe_star_prompt(stream=buf, env={"SGM_CONFIG_DIR": str(tmp_path), **env},
                              interactive=True)
    return shown, buf.getvalue()


def test_first_call_asks_once_and_leaves_marker(tmp_path):
    shown, out = _call(tmp_path)
    assert shown and STAR_URL in out
    assert (tmp_path / STAR_MARKER).exists()


def test_second_call_is_silent(tmp_path):
    _call(tmp_path)
    shown, out = _call(tmp_path)
    assert not shown and out == ""


def test_opt_out_env_is_silent_and_writes_nothing(tmp_path):
    shown, out = _call(tmp_path, SGM_NO_STAR_PROMPT="1")
    assert not shown and out == ""
    assert not (tmp_path / STAR_MARKER).exists()


def test_ci_is_silent(tmp_path):
    shown, out = _call(tmp_path, CI="true")
    assert not shown and out == ""
    assert not (tmp_path / STAR_MARKER).exists()


def test_non_terminal_stdout_is_silent(tmp_path):
    buf = io.StringIO()
    shown = maybe_star_prompt(stream=buf, env={"SGM_CONFIG_DIR": str(tmp_path)},
                              interactive=False)
    assert not shown and buf.getvalue() == ""


def test_unwritable_config_dir_never_raises(tmp_path):
    blocker = tmp_path / "file"
    blocker.write_text("x")
    buf = io.StringIO()
    shown = maybe_star_prompt(stream=buf, env={"SGM_CONFIG_DIR": str(blocker / "sub")},
                              interactive=True)
    assert shown is False
