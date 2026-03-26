# Governance Quality Standards

Use these checks before completing governance work.

## Required Checks

- Verify the active `docs/00.agent-governance/` structure.
- Scan active governance docs for stale path patterns.
- Scan `docs/00.agent-governance/` for Korean text.
- Confirm `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` remain concise.
- Review README accuracy after structural changes.

## Repository Reality Checks

Governance docs must agree with:

- `pyproject.toml`
- `.github/workflows/ci.yml`
- the current repository tree

## Provider Checks

- `CLAUDE.md` must import `AGENTS.md` and `providers/claude.md`.
- `GEMINI.md` must import `AGENTS.md` and `providers/gemini.md`.
