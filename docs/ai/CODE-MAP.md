# Repository map

| Path | Role | Change when |
| --- | --- | --- |
| `AGENTS.md` | Copyable, technology-agnostic agent contract | Baseline rules change |
| `README.md` | Human-facing use and validation instructions | Onboarding or commands change |
| `LICENSE` | MIT license and copyright notice | License terms or holder change |
| `VERSION`, `CHANGELOG.md` | Version source and history | A release or meaningful change occurs |
| `docs/ai/` | This repository's structure and maintenance guide | Layout or workflow changes |
| `scripts/validate_repo.py` | Dependency-free structural checks | Required files or invariants change |
| `.github/workflows/ci.yml` | Push/PR validation | CI behavior changes |

There are no application modules, generated files, or external dependencies. Keep this repository documentation-first; add tooling only to enforce a real invariant.
