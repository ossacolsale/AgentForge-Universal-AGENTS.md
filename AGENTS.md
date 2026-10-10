# AGENTS.md

## Purpose

This is an operating contract for AI agents, not the product specification, functional analysis, architecture manual, plan, or project history. Keep broadly applicable rules here; store detailed knowledge in focused documents and link to authoritative sources from an index when useful.

## Working rules

- Follow the user's request and applicable instruction hierarchy. Surface conflicts rather than silently guessing.
- Inspect the working tree and relevant files before editing. Preserve unrelated changes; never assume the checkout is clean.
- Make the smallest complete change: the smallest change that fulfills the full requested scope, not merely the smallest independently testable increment. Prefer existing patterns; avoid speculative refactors, needless dependencies, duplication, and process for its own sake.
- Use progressive disclosure: read only what the task needs. For a small, self-contained change, inspect target files and local instructions; do not read every index, specification, plan, or test report. For cross-cutting, architectural, ambiguous, high-risk, or resumed work, consult `docs/ai/INDEX.md` if present, then open only relevant entries.
- Consult `docs/ai/SESSION-STATE.md` only when the task may continue unfinished work. Treat it as a handoff, not proof; verify relevant claims against Git, the working tree, and tests. Do not reconstruct unrelated history.
- Protect secrets and sensitive data. Destructive actions, publication, deployment, changes to external services, or material costs require explicit authorization.

## Document roles

- **`AGENTS.md`:** general agent rules, safety, verification, and navigation. Never turn it into functional analysis or a component-by-component manual.
- **Index:** concise list of authoritative documents and when to consult them; do not repeat their contents.
- **Functional specifications:** intended behavior, requirements, acceptance criteria, and focused feature/component analysis. Use an index for substantial products; do not impose needless structure on small projects.
- **Architecture/decisions:** system boundaries, interfaces, durable decisions, and rationale.
- **Plans/test reports:** plans only for substantial multi-stage work; reports record reproducible scenarios, actual results, limitations, and evidence.
- **`SESSION-STATE.md`:** unfinished work only—objective, verified status, blocker/open decision, next action, and essential file/commit references. Keep it to about 150 words or fewer; no conversation logs or facts readily recovered from Git. Mark inactive or clear it when work is complete.

Code and tests describe current implementation; approved specifications describe intended behavior. If they disagree, investigate and report the discrepancy.

## Changes and verification

- Plan only when staged execution materially helps. For a clear, bounded task, complete related implementation work before handing control back to the user. Do not stop for confirmation between dependent subtasks unless blocked by a material ambiguity, a necessary decision, a safety constraint, or an authorization requirement.
- Update documentation when a change makes it inaccurate or alters durable requirements, architecture, interfaces, workflows, or validation. Follow project changelog/version policy; documentation-only changes need no version bump unless policy says otherwise.
- Run checks proportionate to the task and risk. Run fast, relevant automated checks during development and fix failures as they arise. Add regression coverage for bug fixes where practical. Group costly, manual, hardware-dependent, or end-to-end acceptance checks at meaningful integration checkpoints once related changes are ready; run earlier when that materially reduces risk or resolves an important uncertainty. Distinguish automated results from checks that still require user participation.
- Before handoff, verify the requested scope as a whole, run applicable final checks, and consolidate remaining manual checks into a clear checklist. If a genuine blocker prevents completion, report it instead of silently reducing scope. Report only checks actually run.
- Inspect the final diff for unintended changes. Do not add or redesign release automation for unrelated work.

## Release work

This section applies only to builds, packaging, versioning, distribution, and releases. Inspect existing release documentation and workflows first; consult a dedicated release guide only when relevant. Validate the intended tag/version and source revision and the produced artifacts; make reruns safe where applicable and use least-privilege permissions. Publishing, deployment, or external release actions require explicit authorization. Never claim an external release succeeded unless verified.

## Completion

For significant unfinished work, update `docs/ai/SESSION-STATE.md` if present; do not leave completed work marked pending. Finish with a concise summary of changes, checks/results, and unresolved issues or next actions. Never claim unverified checks, builds, releases, or deployments succeeded.

Use `docs/ai/INDEX.md`, when present, to navigate non-trivial documentation. Follow the README and existing configuration/scripts for setup and validation. When adapting this template, replace or remove nonexistent paths and add only real entry points and commands.
