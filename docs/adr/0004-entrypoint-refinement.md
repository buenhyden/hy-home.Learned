# ADR 0004: AI Entrypoint Refinement

> **Status:** Accepted
> **Date:** 2026-03-15
> **Scope:** master
> **layer:** agentic

- **Authors:** buenhyden
- **Deciders:** buenhyden

**Overview (KR):** `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`와 같은 루트 진입점 문서들을 AI Agent가 수행할 규칙(Rule) 중심의 구조로 재정의하고, 지연 로딩(Lazy Loading) 및 스킬 자율성(Skill Autonomy)을 명시적으로 강제하여 에이전트 효율성을 극대화하기 위한 결정입니다.

## Context

Current root entrypoints are primarily informational. While they mention lazy loading, they do not frame their content as a set of enforceable "Rules" that agents MUST parse and follow to discover deeper context.

## Decision

- Refactor `AGENTS.md` to act as the "Shared Instruction Master", defining the base rules for all agents regardless of runtime.
- Refactor `CLAUDE.md` and `GEMINI.md` to serve as model-specific "Ruleset Entrypoints" that lazily load deep context from `docs/agentic/shared/`.
- Ensure all three files explicitly forbid skill restrictions, guiding agents to choose tools based on intent.
- Maintain minimal content in root files, delegating details to Level 1 and Level 2 documents.

## Consequences

- Faster initial parsing for agents (small root files).
- Explicit discovery protocol (agents are "rules-driven" to find more docs).
- Improved consistency across different model runtimes.

## Related

- `[../ard/0001-documentation-hub-architecture.md]`
- `[../adr/0003-lazy-loading-rules.md]`
- `[../prd/2026-03-15-entrypoint-refinement.md]`
