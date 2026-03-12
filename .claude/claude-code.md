# Claude Code Overlay

This manual captures the Claude-specific operating overlay for the repository.
Use it after loading [AGENTS.md](../AGENTS.md) and the
[Shared Governance](shared-governance.md) manual.

## Workflow Order

Use the repository lifecycle workflows as the default execution path:

1. [Pre-Development](../.agent/workflows/workflow-agent-pre-development.md)
2. [During-Development](../.agent/workflows/workflow-agent-during-development.md)
3. [Post-Development](../.agent/workflows/workflow-agent-post-development.md)

For test structure and validation details, use the
[Testing Workflow](../.agent/workflows/Testing/workflow-testing.md).

## Validation Expectations

- The project is `uv`-managed. Run `uv sync` when `pyproject.toml` or `uv.lock`
  changes.
- Match verification to the scope of the change. Common local checks are
  `uv run ruff check .`, `uv run mypy --strict .`, and `uv run pytest` when the
  relevant Python surface changed.
- Use `pre-commit` before handoff when the change is broad enough to affect
  repository-wide formatting or policy enforcement.

## Tool Guidance

- Use `context7` when you need current library documentation.
- Use `next-devtools` only when a task touches Next.js runtime behavior,
  hydration, or browser-console diagnostics.
- Use browser automation and the testing workflow for UI verification rather
  than describing expected behavior without evidence.

## Skill Guidance

- Prefer the active skill registry and repository governance documents before
  inventing a custom workflow.
- Treat the root `CLAUDE.md` as an entrypoint only. Keep reusable detail in this
  manual or in project governance docs.

---
_Last Updated: March 2026_
