# AGENTS.md

## Purpose

This is an operating contract for AI agents, not a specification, architecture manual, plan, or project history. Keep general rules here and detailed knowledge in focused documents, linked from an index when useful.

## Working rules

- Follow the user's request and instruction hierarchy; surface conflicts. Prioritize safety and correctness, then authorized scope and compatibility, then maintainability and simplicity; optimize resource use within those constraints.
- Inspect the working tree and relevant files before editing; preserve unrelated changes.
- Identify the deliverable; implement the simplest complete solution within existing architecture and conventions. Reuse modules, APIs, helpers, and abstractions. Preserve public behavior, compatibility, invariants, and contracts unless authorized otherwise; refactor locally only as needed for integration.
- Keep responsibilities cohesive, coupling low, and interfaces explicit where useful. Avoid excessive fragmentation and unrelated responsibilities in one component. Favor readability, debugging, and incremental change over minimum line count.
- Before adding files, abstractions, dependencies, helpers, validation, or configuration, assess internally whether they meet a present requirement or demonstrably reduce complexity; otherwise omit them. Avoid speculative extensibility and unnecessary frameworks, wrappers, factories, and layers. Remove dead code, duplication, gratuitous indirection, and redundant comments within scope. Handle realistic failures and required contracts; avoid speculative defenses and fallbacks.
- Start with narrow filename, symbol, or text searches and targeted excerpts; expand only as evidence requires. Reuse verified context; avoid repeated scans, calls, reads, unnecessary research, and large outputs. Use tools only to aid implementation or validation. Keep plans and communication brief; never trade necessary investigation or correctness for artificial token limits.
- Use progressive disclosure: for local changes, read target files and local instructions. For cross-cutting, architectural, ambiguous, high-risk, or resumed work, consult `docs/ai/INDEX.md` if present, then only relevant entries. Never require the entire project history.
- Read `docs/ai/SESSION-STATE.md` only to resume unfinished work. Treat it as a handoff, not proof; verify relevant claims against Git, the working tree, and tests.
- Protect secrets and sensitive data. Destruction, publication, deployment, external-service changes, and material costs require explicit authorization.
- Reuse existing CI/CD workflows first. Require a concrete need for new or expanded automation, including full builds, job matrices, scheduled runs, and artifact uploads. Scope triggers to that need, avoid duplicate runs, and retain artifacts only as long as useful. Seek user approval for significant recurring resource use or unrequested operational effects. Preserve required tests, security checks, and compatibility.
- For workflows, storage, or distribution on GitHub, follow the [GitHub Free resource policy](docs/ai/GITHUB-FREE.md).

## Document roles

- **`AGENTS.md`:** general agent rules, safety, verification, and navigation; no functional or component manual.
- **Index:** authoritative documents and when to consult them, without repeating content.
- **Functional specifications:** intended behavior, requirements, acceptance criteria, and focused feature/component analysis. Use an index for substantial products; avoid needless structure for small projects.
- **Architecture/decisions:** system boundaries, interfaces, durable decisions, and rationale.
- **Plans/test reports:** substantial multi-stage plans; reproducible scenarios, actual results, limitations, and evidence.
- **`SESSION-STATE.md`:** unfinished work only—objective, verified status, blocker/open decision, next action, and essential file/commit references. Aim for 150 words or fewer; omit conversation logs and facts recoverable from Git. Clear or mark inactive when complete.

Code and tests describe current implementation; approved specifications describe intended behavior. If they disagree, investigate and report the discrepancy.

## Documentation economy

- Update authoritative documentation only when inaccurate or durable requirements, architecture, contracts, workflows, or validation change. Follow project changelog/version policy; documentation-only changes need no version bump unless required.
- Give each durable fact one authoritative home; link rather than duplicate details, results, or change narratives.
- Keep plans, handoffs, and test summaries concise: reproducible scenarios, actual results, relevant revision/environment, limitations, and stable evidence references; omit activity logs.
- Preserve evidence not reconstructible from Git or automated tests, such as hardware observations, external behavior, migrations, security incidents, and unresolved regressions. Keep history discoverable outside the normal reading path; never expose secrets.

## Changes and verification

- Keep ordinary plans internal; plan explicitly only when staged execution helps. Complete the full authorized task without confirmation between dependent steps. Ask only for material ambiguity, missing authorization, or decisions that cannot be safely inferred.
- Fix issues introduced by the change and critical directly relevant defects. Prioritize blockers, regressions, security, data loss, and required-check failures. Report unrelated or non-blocking findings; avoid unrelated rewrites or release-automation changes.
- Complete coherent edits before the main validation pass. Select the smallest useful checks for behavior, risk, and project policy: focused unit/regression tests for local logic and bugs; integration tests for affected interactions, contracts, persistence, boundaries, or deployment when warranted. Avoid automatic full suites or extensive tests for trivial/documentation changes. Preserve mandatory CI, security, compliance, migration, and safety-critical checks regardless of cost.
- Test meaningful behavior; avoid excessive mocks, brittle implementation assertions, and speculative cases. Investigate failures before retrying; fix causes and rerun affected checks. Broaden only for failures, shared dependencies, architecture changes, or risk; do not repeat unaffected passing checks. Distinguish pre-existing, environmental, and change-induced failures; never count skipped or unavailable checks as passing.
- Review the final diff and full scope for omissions, duplication, contradictions, and unintended changes. Report unverified work and blockers; never silently reduce scope. Final acceptance belongs to the user.

## Release work

For builds, packaging, versioning, distribution, or releases, inspect relevant release documentation and workflows. Validate the intended tag/version, source revision, and artifacts; make reruns safe where applicable and use least privilege. External release actions require explicit authorization and verified results.

## Completion

Stop when the full request is implemented, proportionately verified, critical relevant issues resolved, and limitations reported. Do not continue polishing, refactoring, auditing, or testing without a task-related reason, or stop with material acceptance requirements unmet unless blocked and reported.

For significant unfinished work, update `docs/ai/SESSION-STATE.md` if present. Finish with concise changes, actual checks/results, unverified work, and unresolved issues or next actions. Never claim unverified builds, releases, or deployments succeeded.

Follow the README and existing setup/validation scripts. Adapt to project-specific risks, including regulated, legacy, and real-time systems; remove nonexistent paths and add only real entry points and commands.
