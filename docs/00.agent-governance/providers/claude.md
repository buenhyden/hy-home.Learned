# Claude Provider Notes

This file contains Claude Code-specific runtime behavior only.

## Core Behavior

- Claude Code reads `CLAUDE.md`, not `AGENTS.md` directly.
- Use a thin repository shim in `CLAUDE.md`:
  - `@AGENTS.md`
  - `@./docs/00.agent-governance/providers/claude.md`
- Keep project `CLAUDE.md` concise. Recommended target is under 200 lines.

## Loading And Modularity

- `@path` imports are expanded at session startup.
- For larger rule sets, prefer path-scoped files under `.claude/rules/`.
- Subdirectory `CLAUDE.md` files are loaded on demand when Claude reads files in those areas.

## Governance Boundary

- Keep repository-wide governance in `AGENTS.md` and `docs/00.agent-governance/rules/`.
- Keep this file limited to Claude-specific behavior and caveats.
