# Claude Provider Notes

This file contains Claude Code-specific notes only.

## Core Behavior

- Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so the repository shim must import `AGENTS.md`.
- Keep the root `CLAUDE.md` minimal and let provider detail live here.
- Claude-specific project instructions should stay concise and modular.

## Repository Contract

- The repository shim is:
  - `@AGENTS.md`
  - `@./docs/00.agent-governance/providers/claude.md`
- Root provider behavior must not duplicate repository-wide standards already defined in `AGENTS.md`.

## Notes

- `.claude/rules/` can be used later if the repository needs Claude-only path-scoped rules.
- For this repository, the active governance source of truth is the root bootstrap plus `docs/00.agent-governance/`.
