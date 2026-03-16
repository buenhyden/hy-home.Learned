# ADR 0003: Lazy-Loading Agent Rules

> **Status:** Accepted
> **Date:** 2026-03-15
> **Scope:** master
> **layer:** agentic

- **Authors:** buenhyden
- **Deciders:** buenhyden

**Overview (KR):** AI Agent의 명령어를 한 번에 모두 로드하지 않고, 필요할 때 지연 로딩(Lazy Loading)하는 방식을 채택하여 컨텍스트 효율성을 높이고 성능을 최적화하는 결정입니다.

## Context

Current agent rules in `.agent/rules/` are flat and can lead to context bloat if they grow too large. We need a way to only load relevant instructions based on the current task intent.

## Decision

- Standardize short-form triggers in `.agent/rules/` that point to long-form detail layers.
- Move authoritative long-form instructions to `docs/agentic/`.
- Use the `layer:` metadata to help agents navigate the correct context.

## Consequences

- Reduced initial context overhead for agents.
- Improved maintainability by separating triggers from core logic.
- Slight increase in navigation steps for the AI (agent must follow the link), but this is mitigated by the 9-step reasoning framework.

## Related

- `[../ard/0001-documentation-hub-architecture.md]`
- `[../prd/2026-03-15-governance-hub.md]`
- `[../specs/2026-03-15-metadata-and-trigger-spec.md]`
