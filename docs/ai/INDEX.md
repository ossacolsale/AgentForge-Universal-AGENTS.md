# AI repository guide

This repository publishes a reusable root `AGENTS.md`; it has no application code. Read the [repository map](CODE-MAP.md) before editing. At each new work session, `AGENTS.md` directs Codex to check [`SESSION-STATE.md`](SESSION-STATE.md) for resumable work and verify it against Git. Run `python3 scripts/validate_repo.py` after documentation, metadata, or workflow changes. CI runs this check for pushes and pull requests; releases are intentionally manual and no release workflow exists.
