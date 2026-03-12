# Gemini Directives

This is the Gemini entrypoint for `hy-home-learned`. Load the shared governance
first, then apply the Gemini-specific overlay.

## Load Order

1. [AGENTS.md](AGENTS.md)
2. [Shared Governance](.claude/shared-governance.md)
3. [Gemini Overlay](.claude/gemini-models.md)

## Quick Links

- [Requirements Standard](.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md)
- [Strong Reasoner Rule](.agent/rules/0000-Agents/0002-strong-reasoner-agent.md)
- [Responsible AI Rule](.agent/rules/0100-Standards/0106-responsible-ai.md)
- [AI Safety Rule](.agent/rules/0500-AI_and_ML/0510-ai-safety.md)

## Working Rules

- Planning artifacts come first for multi-file or architectural work.
- Use large context deliberately, but still follow the repository's lazy-loading
  rules.
- Treat this file as the entrypoint only; the detailed Gemini behavior lives in
  `.claude/gemini-models.md`.

---
_Last Updated: March 2026_
