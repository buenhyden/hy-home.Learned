# Refactor Execution Plan

- **Status**: In Progress
- **Scope**: master
- **layer:** common

**Overview (KR):** 문서 경로 복수형 표준화, 루트 문서 강화, 그리고 AI 에이전트 프레임워크 고도화를 실행하기 위한 상세 단계별 계획입니다.

## Context & Introduction

This plan executes the decisions recorded in `ADR 0002` and the requirements in `Governance Hub PRD`. It focuses on direct file modifications to achieve the March 2026 documentation hardening baseline.

## Tasks

### Phase 1: Artifact Creation (Mandatory)

- [x] Create `ADR 0002` for path pluralization.
- [x] Create Documentation Structure `ARD`.
- [x] Create Governance Hub `PRD`.
- [ ] Create Metadata Hardening `Spec`.

### Phase 2: Root Documentation Hardening

- [ ] Update `ARCHITECTURE.md` (Update paths, ensure `layer: architecture`).
- [ ] Update `CODE_OF_CONDUCT.md` (Cleanup metadata).
- [ ] Update `COLLABORATING.md` (Align paths and roles).
- [ ] Update `CONTRIBUTING.md` (Enforce spec-driven rule).
- [ ] Update `OPERATIONS.md` (Update catalog paths).
- [ ] Update `README.md` (Update structure tree and commands).

### Phase 3: Agent Framework Refinement

- [ ] Update `AGENTS.md` (Standardize rules).
- [ ] Update `CLAUDE.md` (Skill autonomy).
- [ ] Update `GEMINI.md` (Planning expectations).
- [ ] Update `docs/agentic/shared/governance.md` & `repository-guide.md`.

## Verification

- `[VAL-001]` All paths in `README.md` structure tree exist on disk.
- `[VAL-002]` `grep -r "docs/plan/" .` returns zero results.
- `[VAL-003]` `AGENTS.md` contains explicit lazy loading and skill autonomy instructions.

## Related

- `[../prd/2026-03-15-governance-hub.md]`
- `[../ard/2026-03-15-documentation-structure.md]`
- `[../adr/0002-path-pluralization.md]`
