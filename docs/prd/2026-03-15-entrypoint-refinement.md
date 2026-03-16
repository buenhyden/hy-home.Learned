# AI Entrypoint Refinement Product Requirements Document (PRD)

> **Status**: Approved
> **Target Version**: v0.2.1
> **Owner**: buenhyden
> **Stakeholders**: buenhyden
> **Scope**: master
> **layer:** product

**Overview (KR):** AI Agent가 저장소에 진입할 때 가장 먼저 접하는 문서들이 지연 로딩과 스킬 자율성 규칙을 명확히 전달하도록 하여, 불필요한 컨텍스트 로딩을 줄이고 에이전트의 수행 능력을 최적화하는 요구사항을 정의합니다.

## Vision

Make `hy-home-learned` the gold standard for agent entrypoint design, where every root file provides a clear, rule-based path to deeper repository knowledge.

## Requirements

- **[REQ-PRD-FUN-04]** `AGENTS.md` must define mandatory reasoning and discovery rules for all agents.
- **[REQ-PRD-FUN-05]** `CLAUDE.md` and `GEMINI.md` must implement lazy loading from `docs/agentic/shared/` specific to their runtime mechanics.
- **[REQ-PRD-FUN-06]** All entrypoints must explicitly state that skills are not restricted.

## Success Criteria

- Agents correctly load only needed sub-manuals from `docs/agentic/`.
- Zero mention of "restricted skills" in root documentation.
- All root entrypoints contain `layer: common` (or appropriate) metadata.

## Related

- `[../ard/0001-documentation-hub-architecture.md]`
- `[../adr/0004-entrypoint-refinement.md]`
