# Claude Code Directives

This is the Claude Code entrypoint for `hy-home-learned`. Load the shared
governance first, then apply the Claude-specific overlay.

## Load Order

1. [AGENTS.md](AGENTS.md)
2. [Shared Governance](.claude/shared-governance.md)
3. [Claude Code Overlay](.claude/claude-code.md)

## Quick Links

- [Pre-Development Workflow](.agent/workflows/workflow-agent-pre-development.md)
- [During-Development Workflow](.agent/workflows/workflow-agent-during-development.md)
- [Post-Development Workflow](.agent/workflows/workflow-agent-post-development.md)
- [Testing Workflow](.agent/workflows/Testing/workflow-testing.md)

## Working Rules

- Prefer the repository's documented workflows, rules, and active skills before
  ad-hoc scripting.
- Keep validation local and explicit for any code or UI change.
- Treat this file as the entrypoint only; the detailed Claude behavior lives in
  `.claude/claude-code.md`.

---
_Last Updated: March 2026_
