# AI Agents Master Guide

This is the shared entrypoint for AI assistants working in `hy-home-learned`.
Start here, then load the shared governance manual and the model-specific
overlay for the active session.

## Required Reading Order

1. [Shared Governance](.claude/shared-governance.md)
2. [Development Guides](docs/guides/README.md)
3. One model overlay:
   - [Claude Code](CLAUDE.md)
   - [Gemini](GEMINI.md)

## Quick Links

- [Agent Governance Index](.claude/README.md)
- [Collaboration Guide](docs/manuals/collaboration-guide.md)
- [ADRs](docs/adr/README.md)
- [ARDs](docs/ard/README.md)
- [PRDs](docs/prd/README.md)
- [Specs](docs/specs/)
- [Plans](docs/plans/)
- [Runbooks](docs/runbooks/)
- [Operations](docs/operations/)

## Non-Negotiables

- State the active persona explicitly using the format required by
  [0018-specialized-agent-personas-standard.md](.agent/rules/0000-Agents/0018-specialized-agent-personas-standard.md).
- Do not start code changes without approved planning and specification context
  from `docs/prd/`, `docs/adr/`, `docs/specs/`, and `docs/plans/`.
- Identify the relevant `.agent/rules/`, `.agent/workflows/`, and active skills
  before execution.
- Use lazy loading: read README or index files first, then only the documents
  needed for the active task.
- Keep changes surgical. Do not expand scope without an explicit request.

---
_Last Updated: March 2026_
