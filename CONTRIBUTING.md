# Contributing

Pick something small, show what you ran, get named. The general terms for all our repos live in
[tonydzi/.github CONTRIBUTING.md](https://github.com/tonydzi/.github/blob/main/CONTRIBUTING.md): you
keep your copyright, there is no CLA, and we answer every issue and PR within 48 hours.

## Where to start

- An open issue labelled `good first issue`, or one you hit yourself: say so in a comment first.
- A bug: an issue with the command you ran and what it printed is already a contribution.
- A fix with a test. A test that stays green when your fix is removed does not count; the suite
  here is written so each one goes red on the bug it guards.

## How I tested

Every PR description carries this block. "Tested, works" is a conclusion we cannot check; ten
pasted lines we can.

````
Platform: <OS, Python version>

```
<the exact commands you ran, for example: python -m pytest tests/test_mcp_server.py -q>
<what they printed, pasted, trimmed only where it is long>
```
````

For a text-only change (README, a docstring) show the before and after of the file. If an AI wrote
your change, say which one and confirm you ran it yourself; that is welcome. Generated code nobody
ran is the one thing we close on sight.

## Credit

- **Every merged PR from outside the maintainers is named in [`CHANGELOG.md`](CHANGELOG.md) by your
  GitHub handle and PR number**, in the release that ships it. A typo fix is a contribution too.
- **An idea from a closed PR is not lost.** If we close your PR and later write the same idea
  ourselves, the commit carries a `Co-authored-by:` trailer for you and the changelog names you.
- **This is checked by a machine, not by memory.** `scripts/credit_gate.py` runs on every push to
  `main` and on every PR. It fails when a merged outside PR has no changelog paragraph with
  `@your-handle` and `#number`, and when a `@handle` in the changelog is not a real GitHub user.
  If the check is red on your own PR, the line it asks for is the thanks we owe you: a maintainer
  adds it before merging. Run it yourself with `python scripts/credit_gate.py --selftest`.

## Setup

```
pip install numpy pytest
python -m pytest -q
```
