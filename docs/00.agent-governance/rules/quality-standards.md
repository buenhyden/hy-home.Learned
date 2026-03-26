# Governance Quality Standards

Use these checks before completing governance tasks.

## Required Checks

- Verify active `docs/00.agent-governance/` structure and routing order.
- Confirm `pre-task-checklist.md` gates were followed.
- Run `path-validation.md` checks for stale paths and broken references.
- Scan `docs/00.agent-governance/` for Korean text.
- Confirm `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` remain concise.
- Review README accuracy after structural or navigation changes.

## Repository Reality Checks

Governance references must agree with:

- `pyproject.toml`
- `.github/workflows/ci.yml`
- current repository tree

## Provider Checks

- `CLAUDE.md` must import `AGENTS.md` and `providers/claude.md`.
- `GEMINI.md` must import `AGENTS.md` and `providers/gemini.md`.
- Provider notes must not duplicate repository-wide governance rules.

## Line-Budget Guidance

- `AGENTS.md`: keep concise, recommended <= 80 lines
- `CLAUDE.md`: thin shim, recommended <= 40 lines
- `GEMINI.md`: thin shim, recommended <= 40 lines
