# AGENTS.md

## Purpose and navigation

Use these rules throughout the repository. A nearer `AGENTS.md` may add scope-specific rules but must not weaken an explicit global requirement. Start here, read [`docs/ai/INDEX.md`](docs/ai/INDEX.md), then inspect only the files relevant to the task; broaden the search when evidence requires it.

## Repository map

- `docs/ai/`: concise architecture and file map for this baseline repository.
- `scripts/validate_repo.py`: dependency-free repository self-check.
- `.github/workflows/`: CI validation; no publishing or release automation.
- `VERSION`, `CHANGELOG.md`: current version and change history.

For another project, replace this map and document its real entry points, configuration, tests, generated files, and validation commands.

## Change rules

- Classify the change first; make the smallest complete, relevant edit.
- Keep code clear, modular, and explicit. Prefer existing capabilities; avoid needless dependencies, abstractions, duplication, and comments that restate code. Comment intent or non-obvious constraints.
- Validate external input, handle errors explicitly, and never expose or commit secrets or sensitive data.
- Edit sources of truth, regenerate derived files when needed, and document that relationship.
- Keep user and AI documentation accurate. Update `docs/ai/` when structure, ownership, or workflows change; add a concise changelog entry for every meaningful change.

## Verification

For code changes, run the complete applicable suite: relevant tests plus project-defined lint, formatting, type, static, build, package, configuration, dependency, security, and workflow checks. Add or update regression coverage for bug fixes. Choose checks that match the project's architecture and risk; do not claim checks you did not run. Documentation-only edits need consistency and repository checks, not irrelevant code checks.

## Versioning and releases

Use the project's declared version source and Semantic Versioning unless its ecosystem specifies otherwise: breaking change = major, compatible capability = minor, compatible fix = patch. Update all exposed version metadata and the changelog for code changes; documentation-only edits do not require a version bump. Start new projects at `0.1.0`.

Add or activate release automation only after the user explicitly requests it. That request authorizes the pipeline, not publishing, tagging, or deployment; those actions need their own explicit authorization. Keep authorized release logic documented and ensure it gates on valid builds and tests where feasible.

## Completion

Finish only when the requested change, relevant tests and checks, version/changelog, affected documentation, generated artifacts, and workflow consistency are complete. For this documentation repository, run `python3 scripts/validate_repo.py`.
