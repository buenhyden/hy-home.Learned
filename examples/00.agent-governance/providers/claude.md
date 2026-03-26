# Claude Provider Notes (March 2026)

## Scope

This file contains Claude Code-specific guidance only. Repository-wide rules live in the shared fragments imported by [`../../CLAUDE.md`](/CLAUDE.md).

## Memory Hierarchy

Claude Code loads `CLAUDE.md` files in this order (lowest to highest precedence):

| File                       | Scope                 | Notes                                                    |
| -------------------------- | --------------------- | -------------------------------------------------------- |
| `~/.claude/CLAUDE.md`      | Global — all projects | User-wide preferences; personal defaults                 |
| `./CLAUDE.md` (repo root)  | Project — shared      | Checked into git; applies to all team members            |
| `./.claude.local.md`       | Project — personal    | Gitignored; use for local overrides not shared with team |
| `<subdirectory>/CLAUDE.md` | Directory             | Loaded automatically when working within that directory  |

## Claude Code Instructions

- Keep the root `CLAUDE.md` thin and import shared fragments with `@` references.
- Prefer parent-to-child memory hierarchy: root file for universal rules, subdirectory files for local detail.
- Use `.claude.local.md` for personal preferences (API keys, editor settings). Add to `.gitignore`.
- Preserve context by loading the owning layer router before loading adjacent layers.
- During a session, press `#` to have Claude automatically incorporate session learnings directly into `CLAUDE.md`.
- **Skill Autonomy**: Claude MUST utilize any available skill (e.g., `writing-plans`, `executing-plans`, `doc-coauthoring`) .
- **Persona Activation**: Declare `Layer` and `Stage` (01-11) upon session start.
- **Taxonomy First**: Anchoring implementation to `docs/04.specs/` is non-negotiable.

## Recommended Workflows

 Claude SHOULD utilize the following workflows for governance maintenance:

- `@/agent-md-refactor`: Use when `AGENTS.md` or common rules become bloated (>500 tokens).
- `@/claude-md-improver`: Use for periodic audits of `CLAUDE.md` and related fragments.
- **Post-Refactor**: Always invoke `distill` or `polish` skills to ensure high-quality documentation.

## Import Syntax

Use `@` references in `CLAUDE.md` to import shared fragments at session start:

```text
@docs/00.agent-governance/rules/bootstrap.md
@docs/00.agent-governance/rules/persona.md
@docs/00.agent-governance/rules/standards.md
```

Paths are resolved relative to the repository root. Imports are loaded once at session start.

## References

- Anthropic Claude Code memory: <https://docs.anthropic.com/en/docs/claude-code/memory>
