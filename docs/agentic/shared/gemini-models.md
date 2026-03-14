# Gemini Overlay

> **layer:** agentic

This file contains Gemini-specific operating detail. The root
[GEMINI.md](../GEMINI.md) is the runtime entrypoint; reusable detail lives here.

## Planning Expectations

- For multi-file work, deep refactors, or architectural changes, keep planning
  artifacts current in the active session and in [docs/plans/](../docs/plans/).
- Align planning behavior with [Requirements Standard](../docs/agentic/pillar.md).

## Context Handling

- Gemini may hold large context, but it must still follow the repository's
  lazy-loading rules.
- Start from [docs/README.md](../docs/README.md), then open only the relevant
  index and the specific target file.
- Treat external `task.md` and `implementation_plan.md` artifacts as working
  scratchpads, and mirror stable repository decisions into `docs/plans/`.

## Safety and Governance

- Follow
  [0106-responsible-ai.md](../.agent/rules/0100-Standards/0106-responsible-ai.md)
  and
  [0510-ai-safety.md](../.agent/rules/0500-AI_and_ML/0510-ai-safety.md)
  for prompt safety, review posture, and validation.
- Do not let high context capacity bypass repository governance, plan gates, or
  evidence-based verification.

---

_Last Updated: March 2026_
