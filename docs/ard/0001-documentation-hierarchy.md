# Documentation Hierarchy Architecture Reference Document

- **Status**: Approved
- **Owner**: buenhyden
- **Scope**: master
- **layer:** agentic
- **PRD Reference**: `[../prd/0001-agentic-hub-refinement.md]`
- **ADR References**: `[../adr/0001-documentation-restructuring.md]`

**Overview (KR):** 이 문서는 프로젝트의 문서 계층 구조와 각 폴더의 역할을 정의합니다. 모든 문서는 `layer:` 메타데이터를 포함해야 하며, 정해진 템플릿을 준수해야 합니다.

## Summary

This ARD defines the structural layout and governance rules for documentation within the `hy-home.Learned` ecosystem. It ensures that humans and AI agents have a predictable path for requirements, specs, and operational data.

## Boundaries

- **Owns**: The directory structure under `docs/` and the metadata standards for MD files.
- **Consumes**: Engineering standards and collaboration guide triggers.
- **Does Not Own**: Actual code implementations or infrastructure configuration.

## Ownership

- **Primary owner**: buenhyden
- **Primary artifacts**: `[docs/]`, `[templates/]`
- **Operational evidence**: `[../runbooks/documentation-maintenance.md]`

## Related

- `[../prd/0001-agentic-hub-refinement.md]`
- `[../specs/2026-03-14-lazy-loading-implementation.md]`
- `[../plans/2026-03-14-documentation-migration.md]`
- `[../adr/0001-documentation-restructuring.md]`

## 4. Architecture & Tech Stack Decisions

### 4.1 Component Architecture

The documentation is organized into clear functional layers:

1. **Master Layer**: Global docs in root and `docs/`.
2. **Detail Layer**: `docs/agentic/` for deep agentic logic.
3. **Execution Layer**: `docs/specs/` and `docs/plans/`.
4. **Operations Layer**: `docs/runbooks/` and `docs/operations/`.

### 10. Source-of-Truth Map

| Scope   | Canonical Document                            | Role                             |
| ------- | --------------------------------------------- | -------------------------------- |
| master  | `docs/ard/0001-documentation-hierarchy.md`    | Top-level architecture authority |
| feature | `docs/specs/`                                 | Implementation detail            |
