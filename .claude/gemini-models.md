# Gemini Overlay

This manual captures the Gemini-specific operating overlay for the repository.
Use it after loading [AGENTS.md](../AGENTS.md) and the
[Shared Governance](shared-governance.md) manual.

## Planning Expectations

- For multi-file work, deep refactors, or architectural changes, keep `task.md`
  and `implementation_plan.md` current alongside the repository plan in
  `docs/plans/`.
- Align planning behavior with
  [0120-requirements-and-specifications-standard.md](../.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md)
  and the
  [workflow-agent-pre-development.md](../.agent/workflows/workflow-agent-pre-development.md)
  contract.
- Use `sequential-thinking` for deep architectural analysis, debugging, or any
  task where the reasoning chain needs to stay explicit.

## Context Handling

- Gemini can synthesize broad repository context, but it must still follow the
  lazy-loading rules from the shared governance manual.
- Read only the documents needed for the active task item. High context
  capacity is not permission to bulk-load the repo.
- When a task produces a stable, reusable pattern, update the relevant `TIL/`
  node or create one if the project workflow requires it.

## Safety and Governance

- Follow
  [0106-responsible-ai.md](../.agent/rules/0100-Standards/0106-responsible-ai.md)
  and
  [0510-ai-safety.md](../.agent/rules/0500-AI_and_ML/0510-ai-safety.md)
  for prompt safety, validation, and review posture.
- Treat the root `GEMINI.md` as an entrypoint only. Keep reusable detail in this
  manual or in project governance docs.

---
_Last Updated: March 2026_
