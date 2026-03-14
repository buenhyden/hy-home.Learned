# Incident: Documentation Drift and AI Instruction Fragmentation

- **Status**: Resolved
- **Priority**: SEV-2
- **layer:** agentic
- **Date**: 2026-03-14

**Overview (KR):** 프로젝트 문서 구조가 파편화되어 AI Agent의 정확도가 떨어지는 현상이 발견되었으며, 이를 해결하기 위해 문서 구조 재편Incident를 생성합니다.

## Summary

AI agents were observed using outdated instructions from `.agent/rules/` while new standards existed in root MD files. This drift caused inconsistent reasoning.

## Timeline

- **09:00**: Agent observed disregarding `ARCHITECTURE.md`.
- **10:00**: Issue traced to fragmented instruction triggers.
- **11:00**: Incident SEV-2 declared.

## Resolution

- Planned a full documentation restructuring and agentic hub centralization.
- Implemented lazy-loading triggers to ensure single source of truth.

## Related

- **Postmortem**: `[../postmortems/2026-03-14-hierarchy-migration.md]`
- **Plan**: `[../../plans/2026-03-14-documentation-migration.md]`
