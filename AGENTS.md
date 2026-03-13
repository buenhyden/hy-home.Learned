# AI Agents Master Guide

This is the shared, vendor-neutral entrypoint for AI assistants working in
`hy-home-learned`. Start here, then load the repository docs hub and the
model-specific runtime file for the active session. Keep the root entrypoints
minimal; `.claude/` is the authoritative detail layer.

## Quick Reference

- **Environment:** Python 3.13+, `uv`
- **Sync deps:** `uv sync --dev`
- **Lint:** `uv run ruff check .`
- **Typecheck:** `uv run ty check`
- **Test:** `uv run pytest`
- **Hooks:** `uv run pre-commit install`

## Required Reading Order

1. [Documentation Hub](docs/README.md)
2. [Shared Agent Governance](.claude/shared-governance.md)
3. [Repository Operating Guide](.claude/repository-guide.md)
4. One model runtime entrypoint:
   - [Claude Code](CLAUDE.md)
   - [Gemini](GEMINI.md)

## Knowledge Navigation

- [ADRs](docs/adr/README.md)
- [ARDs](docs/ard/README.md)
- [PRDs](docs/prd/README.md)
- [Specs](docs/specs/README.md)
- [Plans](docs/plans/README.md)
- [Runbooks](docs/runbooks/README.md)
- [Operations](docs/operations/README.md)
- [Shared `.claude` Index](.claude/README.md)

## Non-Negotiables

- State the active persona explicitly using the sentence required by
  [0018-specialized-agent-personas-standard.md](.agent/rules/0000-Agents/0018-specialized-agent-personas-standard.md).
- Do not begin code changes without approved context from `docs/prd/`,
  `docs/adr/`, `docs/specs/`, and `docs/plans/`, as required by
  [0120-requirements-and-specifications-standard.md](.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md).
- Identify the relevant `.agent/rules/`, `.agent/workflows/`, and skills before
  execution.
- Skills are not restricted by this file. Agents must choose the skills that fit
  the task instead of forcing a narrow whitelist.
- Follow lazy loading: read index documents first, then load only the specific
  file needed for the current task.
- Keep execution surgical. Do not expand scope without an explicit request.
- Use `docs/runbooks/` and `docs/operations/` for operational records. Do not
  reintroduce stale parallel paths such as top-level `specs/` or `runbooks/`
  unless the repository structure changes first.

---

_Last Updated: March 2026_
