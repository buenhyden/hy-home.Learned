# Agent Governance Manuals

This directory holds the detailed governance manuals behind the three root
instruction files: [AGENTS.md](../AGENTS.md), [CLAUDE.md](../CLAUDE.md), and
[GEMINI.md](../GEMINI.md).

## Reading Order

1. Start with [Shared Governance](shared-governance.md).
2. Open the model-specific overlay for the active tool:
   - [Claude Code Overlay](claude-code.md)
   - [Gemini Overlay](gemini-models.md)
3. Use the repository collaboration docs for project-specific overrides:
   - [Collaboration Guide](../docs/manuals/collaboration-guide.md)
   - [Development Guides](../docs/guides/README.md)

## Scope

- Keep the root files short and stable.
- Put reusable governance in this directory.
- Put model-specific detail in the matching overlay file.
- Treat this directory as the authoritative location for shared agent
  instruction content.

---
_Last Updated: March 2026_
