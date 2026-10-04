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

When adapting this guide for a software project that distributes software, provide a usable GitHub Actions release pipeline when work concerns building, packaging, versioning, distribution, or release. Keep release readiness separate from actually publishing packages, deploying, or creating releases: those external actions need explicit authorization. Do not add release automation to documentation-only repositories that do not distribute software.

A release pipeline should separate target validation, test/build, artifact packaging, artifact validation, and GitHub Release publishing. Publishing must depend on successful test/build and artifact checks, and use `contents: write` only in the publish job when needed. Use immutable SemVer tags as release identities. Prefer both tag-push and `workflow_dispatch` with a tag input. For a manual run, verify the tag exists, resolve and check out that tag, validate its SemVer and package versions, and rebuild artifacts from that commit rather than from the default branch. A corrected workflow on the default branch must be able to rerun the same tag without moving or recreating it or relying on artifacts from an earlier run.

Make publishing safe to retry: do not create a duplicate GitHub Release when one already exists. Serialize concurrent publishes for the same tag. Validate each package using its actual format, with coverage for valid, corrupt or truncated, incomplete, and prohibited local or sensitive contents. Produce versioned artifacts and checksums when applicable; document release notes and recognize prereleases. Keep external registry publishing as a separate, explicitly authorized step. Document how to create a release and rerun an existing tag, and update AI instructions when release or CI workflows change.

Before completing release-pipeline work, inspect all workflows and verify their triggers, permissions, dependencies, artifact paths and checks, and that manual reruns check out the requested tag. Run applicable checks and inspect the final diff. Report whether the pipeline was validated locally; do not imply that a release was published or verified on GitHub unless that actually happened.

## Completion

Finish only when the requested change, relevant tests and checks, version/changelog, affected documentation, generated artifacts, and workflow consistency are complete. For this documentation repository, run `python3 scripts/validate_repo.py`.
