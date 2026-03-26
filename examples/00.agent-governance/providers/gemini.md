# Gemini Provider Notes (March 2026)

## Scope

This file contains Gemini CLI-specific guidance only. Repository-wide rules live in the shared fragments imported by [`../../GEMINI.md`](/GEMINI.md).

## Context File Hierarchy

Gemini CLI loads context files in this order (lowest to highest precedence):

| File                       | Scope                 | Notes                                                                     |
| -------------------------- | --------------------- | ------------------------------------------------------------------------- |
| `~/.gemini/GEMINI.md`      | Global — all projects | User-wide preferences; personal defaults                                  |
| `./GEMINI.md` (repo root)  | Project — shared      | Checked into git; applies to all team members                             |
| `<subdirectory>/GEMINI.md` | Directory             | JIT-loaded when a tool accesses a file in that directory or its ancestors |

## Gemini CLI Guidance

- Keep the root `GEMINI.md` thin and use `@file`-style imports for shared fragments.
- Use hierarchical context discovery: root file for universal rules, subdirectory files for local task context.
- Prefer on-demand loading through the owning layer router instead of broad repository ingestion.
- MCP server integrations are configured in `.gemini/settings.json` under the `mcpServers` key.
- Sandboxing is **opt-in**, not the default. Enable with `-s` / `--sandbox` flag or `GEMINI_SANDBOX=true`.
- **Skill Autonomy**: Gemini MUST utilize any available skill (e.g., `writing-plans`, `executing-plans`, `doc-coauthoring`).
- **Persona Activation**: Always declare `Layer` and `Stage` (01-11) before starting any implementation task.
- **Taxonomy First**: Reject any task that bypasses `Stage 01 (PRD)` or `Stage 04 (Spec)` unless explicitly overridden.

## Core Competencies

 Gemini MUST prioritize the following skills for governance tasks:

- `prompt-engineer`: Use to optimize complex governance instructions for context-window efficiency.
- `writing-plans`: Mandatory for any refactoring or supplementary documentation task.

## Import Syntax

Use `@file` references in `GEMINI.md` to import shared fragments:

```text
@docs/00.agent-governance/rules/bootstrap.md
@docs/00.agent-governance/rules/persona.md
@docs/00.agent-governance/rules/standards.md
```

Paths are resolved relative to the repository root.

## References

- Gemini CLI context files (GEMINI.md): <https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md>
- Gemini CLI settings: <https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/settings.md>
- Gemini CLI MCP integration: <https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md>
