# AGENTS.md

## Purpose

This is a short operating contract and navigation map—not the product specification, architecture manual, implementation plan, or project history. Keep only rules that matter to most tasks. Put detailed project knowledge in focused documents and link to it from an index.

## Default behavior

- Follow the user's request and the applicable instruction hierarchy. More-specific repository instructions may add detail; surface conflicts instead of silently guessing.
- Inspect the current working tree and relevant files before editing. Preserve unrelated user changes; do not assume the checkout is clean.
- Make the smallest complete change. Prefer existing patterns; avoid speculative refactors, needless dependencies, duplicate explanations, and process for its own sake.
- Use progressive disclosure: inspect only the context needed for the task, then broaden the search when uncertainty or evidence warrants it.
- Protect secrets and sensitive data. Do not perform destructive operations, publish, deploy, modify external services, or incur material costs without explicit authorization.

## Find the right context

- For a small, self-contained change, inspect the target files and applicable local instructions. Do not read every index, specification, plan, or test report by default.
- For cross-cutting, architectural, ambiguous, or high-risk work—or when resuming unfinished work—consult `docs/ai/INDEX.md` if present, then open only relevant entries.
- Consult `docs/ai/SESSION-STATE.md` when the task may continue active work. Treat it as a handoff, not proof; verify important claims against the working tree, Git, and relevant tests. Do not reconstruct unrelated history.
- Prefer targeted file/term searches to reading entire documentation trees. Before creating a document, find its proper existing home.
- Give each durable fact one authoritative home. Summarize only what the reader needs and link to the source; avoid parallel copies that can drift.

## Document responsibilities

- **`AGENTS.md`** — broadly applicable agent rules, safety, verification expectations, and pointers. Never turn it into functional analysis or a component-by-component manual.
- **Documentation index** — a concise catalogue of authoritative documents and when to read them; do not repeat their contents.
- **Functional/product specifications** — intended behavior, requirements, acceptance criteria, and focused per-feature or per-component analysis. For a substantial product, maintain an index linking to these focused specifications.
- **Architecture/decision records** — system boundaries, interfaces, durable decisions, and rationale.
- **Plans** — next steps for substantial multi-stage work only; mark completed plans so they are not mistaken for active work.
- **Test reports** — reproducible scenarios, environment, actual results, limitations, and evidence.
- **`SESSION-STATE.md`** — active unfinished work only: objective, verified status, blocker/open decision, next action, and essential file/commit references. Aim for 150 words or fewer. No conversation logs, general summaries, or facts readily recovered from Git; mark inactive or clear it when work is complete.

Source code and tests describe current implementation; approved specifications describe intended behavior. If they disagree, investigate and report the discrepancy rather than silently treating either as proof of the other.

## Change and verification

- Write a plan only when the task is substantial or risky enough to benefit from staged execution. Keep it proportional; do not maintain duplicate plans and status narratives.
- Update documentation only when the change makes it inaccurate or changes durable requirements, architecture, interfaces, workflows, or validation. Follow existing changelog/version conventions for user-visible or release-relevant changes; documentation-only edits do not need a version bump unless project policy says otherwise.
- Run checks appropriate to the change and its risk: targeted checks for narrow changes, broader suites for cross-cutting or high-risk work. Add regression coverage for bug fixes where practical. Report only checks actually run and state what was not run.
- Inspect the final diff for unintended changes and confirm affected documentation matches the implementation and evidence. Do not add or redesign release automation for unrelated work.

## Handoff and completion

When significant work remains unfinished, update `docs/ai/SESSION-STATE.md` using the short format above. Do not leave a completed task marked as pending. Finish with a concise summary of changes, checks/results, and unresolved issues or next actions. Never claim an unverified test, build, release, or deployment succeeded.

## Repository entry point

Use `docs/ai/INDEX.md`, when present, to navigate non-trivial project documentation. Follow the repository README and existing configuration/scripts for setup and validation. When copying this template into another project, replace or remove nonexistent paths; add only the real entry points and commands an agent needs.
