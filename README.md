# AgentForge Universal AGENTS

A compact, reusable operating guide for AI coding agents. The root [`AGENTS.md`](AGENTS.md) contains operating rules and navigation guidance; it is not a project's functional specification.

## Use

Copy `AGENTS.md` into a project's root, then adapt its entry points, documentation links, and validation guidance to that project. Keep requirements and acceptance criteria in focused functional specifications, with detailed architecture and test evidence in their own documents when needed. For a substantial project, keep an index that points to those authoritative documents; do not make every task read them all. Keep `AGENTS.md` concise and link to relevant context.

When adapting the template, avoid creating unconditional obligations to update changelogs, milestones, test reports, or handoffs after every commit. Update only authoritative documents actually affected by a change, respecting the project's own release policy. Keep one source of truth per durable fact, and store unique historical or manual-test evidence separately from short operational summaries. This guidance does not replace required security, compliance, or recovery records.

This repository's document roles and file locations are summarized in [`docs/ai/INDEX.md`](docs/ai/INDEX.md). See [version](VERSION), [changelog](CHANGELOG.md), and the [MIT license](LICENSE).

## Validate this repository

Requires Python 3; no third-party packages are needed.

```sh
python3 scripts/validate_repo.py
python3 -B -m unittest discover -s tests -v
```

The validator reports oversized agent instructions, index, or session-state files as **advisories** only; they do not fail validation. Suggested limits are heuristics, not mandatory requirements, and should not override project-specific needs. GitHub Actions runs validation and unit tests on pushes and pull requests. There is no release workflow.
