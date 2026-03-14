# AI Agents Master Guide

This is the shared, vendor-neutral entrypoint for AI assistants working in
`hy-home-learned`. Start here, then load the repository docs hub and the
model-specific runtime file for the active session. Keep the root entrypoints
minimal; `docs/agentic/` is the authoritative detail layer.

## Quick Reference

- **Environment:** Python 3.13+, `uv`
- **Sync deps:** `uv sync --dev`
- **Lint:** `uv run ruff check .`
- **Typecheck:** `uv run ty check`
- **Test:** `uv run pytest`
- **Hooks:** `uv run pre-commit install`

## Required Reading Order

1. [Documentation Hub](docs/README.md)
2. [Shared Agent Governance](docs/agentic/shared/shared-governance.md)
3. [Repository Operating Guide](docs/agentic/shared/repository-guide.md)
4. One model runtime entrypoint:
   - [Claude Code](CLAUDE.md)
   - [Gemini](GEMINI.md)

## Knowledge Navigation

- [ADRs](docs/adr/)
- [ARDs](docs/ard/)
- [PRDs](docs/prd/)
- [Specs](docs/specs/)
- [Plans](docs/plans/)
- [Runbooks](docs/runbooks/)
- [Operations](docs/operations/)
- [Agentic Hub](docs/agentic/README.md)

## Non-Negotiables

- State the active persona explicitly using the sentence required by
  [0018-specialized-agent-personas-standard.md](.agent/rules/0000-Agents/0018-specialized-agent-personas-standard.md).
- Do not begin code changes without approved context from `docs/prd/`,
  `docs/adr/`, `docs/specs/`, and `docs/plans/`, as required by
  [Requirements Standard](docs/agentic/pillar.md).
- Identify the relevant `.agent/rules/`, `.agent/workflows/`, and skills before
  execution.
- Skills are not restricted by this file. Agents must choose the skills that fit
  the task instead of forcing a narrow whitelist.
- Follow lazy loading: read index documents first, then load only the specific
  file needed for the current task.
- Keep execution surgical. Do not expand scope without an explicit request.
- Use `docs/runbooks/` and `docs/operations/` for operational records.

---

_Last Updated: March 2026_
