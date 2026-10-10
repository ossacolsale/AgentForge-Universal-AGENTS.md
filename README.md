# AgentForge Universal AGENTS

A compact, reusable operating guide for AI coding agents. The root [`AGENTS.md`](AGENTS.md) contains operating rules and navigation guidance; it is not a project's functional specification.

## Use

Copy `AGENTS.md` into a project's root, then adapt its entry points, documentation links, and validation guidance to that project. Keep requirements and acceptance criteria in focused functional specifications, with detailed architecture and test evidence in their own documents when needed. For a substantial project, keep an index that points to those authoritative documents; do not make every task read them all. Keep `AGENTS.md` concise and link to relevant context.

This repository's document roles and file locations are summarized in [`docs/ai/INDEX.md`](docs/ai/INDEX.md). See [version](VERSION), [changelog](CHANGELOG.md), and the [MIT license](LICENSE).

## Validate this repository

Requires Python 3; no third-party packages are needed.

```sh
python3 scripts/validate_repo.py
```

GitHub Actions runs the same check on pushes and pull requests. There is no release workflow.
