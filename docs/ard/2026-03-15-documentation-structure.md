# Documentation Structure ARD

- **Status**: Approved
- **Owner**: buenhyden
- **Scope**: master
- **layer:** common
- **PRD Reference**: `[../prd/2026-03-15-governance-hub.md]`
- **ADR References**: `[../adr/0002-path-pluralization.md]`

**Overview (KR):** 프로젝트의 문서 계층 구조와 표준화된 메타데이터 형식을 정의하여, AI 에이전트와 인간 협업자가 일관된 방식으로 문서를 관리할 수 있도록 합니다.

## Summary

This document defines the canonical directory structure and metadata requirements for all artifacts in this repository as of March 2026.

## Boundaries

- **Owns**: Directory naming conventions and hierarchy within `docs/` and root.
- **Consumes**: Requirements from `AGENTS.md` regarding lazy loading.
- **Does Not Own**: Individual content within specific domain documents.

## Ownership

- **Primary owner**: buenhyden
- **Primary artifacts**: `[docs/]`, `[templates/]`
- **Operational evidence**: `N/A`

## 4. Architecture & Tech Stack Decisions

### 4.1 Component Architecture

Standardized plural paths for documentation categories:

- `docs/adr/`: Architecture Decision Records.
- `docs/ard/`: Architecture Reference Documents.
- `docs/prd/`: Product Requirements Documents.
- `docs/specs/`: Technical Specifications.
- `docs/plans/`: Execution and Implementation Plans.
- `docs/runbooks/`: Operational and Maintenance Runbooks.
- `docs/operations/incidents/`: Live incident records.
- `docs/operations/postmortems/`: Post-incident blameless analysis.

### 4.2 Metadata Standard

Every markdown file MUST include high-level metadata:

- **`layer:`**: Specifies the functional layer (e.g., `common`, `architecture`, `backend`, `frontend`, `infra`, `mobile`, `product`, `qa`, `security`).
- **Placement**: Usually as a top-level block quote or in YAML frontmatter.

## Related

- `[../prd/2026-03-15-governance-hub.md]`
- `[../specs/2026-03-15-metadata-hardening.md]`
- `[../adr/0002-path-pluralization.md]`
