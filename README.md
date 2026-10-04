# AgentForge Universal AGENTS

A compact, reusable operating guide for AI coding agents. The root [`AGENTS.md`](AGENTS.md) is the copyable baseline; [`docs/ai/`](docs/ai/INDEX.md) explains this repository and its self-check.

## Use

Copy `AGENTS.md` into a project's root, then adapt its repository map and validation references to that project. Keep it generic where possible and specific where evidence supports it. See [version](VERSION) and [changelog](CHANGELOG.md).

## Validate this repository

Requires Python 3; no third-party packages are needed.

```sh
python3 scripts/validate_repo.py
```

GitHub Actions runs the same check on pushes and pull requests. There is no release workflow.
