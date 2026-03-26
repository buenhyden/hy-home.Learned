# Gemini Provider Notes

This file contains Gemini CLI-specific runtime behavior only.

## Core Behavior

- Gemini CLI loads context hierarchically from `GEMINI.md` files.
- Typical load order:
  1. Global: `~/.gemini/GEMINI.md`
  2. Project root and ancestors up to repository root
  3. Subdirectories under the current working directory
- Use a thin repository shim in `GEMINI.md`:
  - `@./AGENTS.md`
  - `@./docs/00.agent-governance/providers/gemini.md`

## Imports And Memory

- Use `@file` imports to modularize large context safely.
- Use `/memory show` and `/memory refresh` to inspect and reload active context.
- `context.fileName` customization is optional fallback behavior, not a repository requirement.

## Governance Boundary

- Keep repository-wide governance in `AGENTS.md` and `docs/00.agent-governance/rules/`.
- Keep this file limited to Gemini-specific loading and runtime behavior.
