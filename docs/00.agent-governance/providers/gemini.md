# Gemini Provider Notes

This file contains Gemini CLI-specific notes only.

## Core Behavior

- Gemini CLI uses hierarchical `GEMINI.md` files as instructional memory.
- `@file` imports are the preferred way to keep `GEMINI.md` modular.
- Do not depend on custom local `context.fileName` settings for repository correctness.

## Repository Contract

- The repository shim is:
  - `@./AGENTS.md`
  - `@./docs/00.agent-governance/providers/gemini.md`
- Root provider behavior must stay thin and should not duplicate repository-wide standards already defined in `AGENTS.md`.

## Notes

- Sandbox behavior is a provider runtime concern, not a repository governance rule.
- The active repository governance source of truth is the root bootstrap plus `docs/00.agent-governance/`.
