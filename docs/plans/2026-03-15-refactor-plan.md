# Documentation Refactor Plan

> **Status**: In Progress
> **Scope**: master
> **layer:** common

**Overview (KR):** 문서 메타데이터 표준화와 AI Agent 명령어 지연 로딩 구현을 위한 단계별 실행 계획입니다.

## Tasks

### Phase-style task list

1. **Phase 1: Metadata Standardization**: Apply `layer:` key to all target files.
2. **Phase 2: Trigger Implementation**: Replace fat rules in `.agent/rules/` with lightweight links to `docs/agentic/`.
3. **Phase 3: Root Cleanup**: Streamline README and ARCHITECTURE to focus on high-level goals.

## Verification

- `[VAL-REF-001]` Grep for `layer:` in all `docs/` files.
- `[VAL-REF-002]` Verify links in `.agent/rules/` point to existing files in `docs/agentic/`.

## References

- `[../prd/2026-03-15-governance-hub.md]`
- `[../specs/2026-03-15-metadata-and-trigger-spec.md]`
- `[../ard/0001-documentation-hub-architecture.md]`
