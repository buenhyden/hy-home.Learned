# Claude Code Overlay

> **layer:** agentic

This file contains Claude-specific operating detail. The root
[CLAUDE.md](../CLAUDE.md) is the runtime entrypoint; reusable detail lives here.

## Workflow Order

1. [Pre-Development](../.agent/workflows/workflow-agent-pre-development.md)
2. [During-Development](../.agent/workflows/workflow-agent-during-development.md)
3. [Post-Development](../.agent/workflows/workflow-agent-post-development.md)
4. [Testing Workflow](../.agent/workflows/Testing/workflow-testing.md) when the
   task requires explicit verification structure

## Validation Expectations

- Match verification to the scope of the change.
- If Python dependency metadata changes, run `uv sync`.
- Use local checks such as `uv run ruff check .`, `uv run mypy --strict .`, and
  `uv run pytest` only when the touched surface justifies them.
- Use `pre-commit` when the change is broad enough to affect repository-wide
  formatting or policy gates.

## Tool Guidance

- Use `context7` when current library documentation is required.
- Use `next-devtools` only when a task involves Next.js runtime behavior,
  hydration, or browser-side diagnostics.
- Use browser automation or the testing workflow for UI verification instead of
  relying on unevidenced descriptions.

## Skills

- Prefer the repository skill registry and [Agentic Docs](../docs/agentic/README.md) before inventing an ad-hoc workflow.
- Do not limit skill choice unless a task explicitly requires a narrower path. Agents must choose the skill that best fits the intended purpose.

---

_Last Updated: March 2026_
