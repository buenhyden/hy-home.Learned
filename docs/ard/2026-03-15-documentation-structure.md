# Documentation Hub Architecture Reference Document

- **Status**: Approved
- **Owner**: buenhyden
- **Scope**: master
- **layer:** common
- **PRD Reference**: `[../prd/2026-03-15-governance-hub.md]`
- **ADR References**: `[../adr/0001-lazy-loading-rules.md]`

**Overview (KR):** 본 저장소의 문서 구조를 4계층(Level 0-3)으로 정의하고, 각 문서의 역할과 위치를 명확히 하여 AI와 사람이 효율적으로 협업할 수 있는 구조를 설명합니다.

## Summary

This ARD defines the global documentation hierarchy for `hy-home-learned`, ensuring a standardized path from high-level policy to low-level implementation.

## Boundaries

- **Owns**: Directory structure under `docs/` and root `.md` files.
- **Consumes**: Metadata rules and agent instruction triggers.
- **Does Not Own**: External third-party documentation.

## Ownership

- **Primary owner**: buenhyden
- **Primary artifacts**: `docs/`, `ARCHITECTURE.md`, `README.md`
- **Operational evidence**: `N/A`

## 1. Component Architecture

The documentation is organized into 4 logical tiers:

1. **Level 0 (Root)**: High-level entry points (`README.md`, `ARCHITECTURE.md`).
2. **Level 1 (Indices)**: Governance and operational indices (`OPERATIONS.md`, `docs/agentic/README.md`).
3. **Level 2 (Management)**: Standards and protocols (`docs/agentic/standards/`).
4. **Level 3 (Execution)**: Temporal artifacts for specific tasks (`docs/specs/`, `docs/plans/`, `docs/adr/`).

## 10. Source-of-Truth Map

| Scope   | Canonical Document                            | Role                             |
| ------- | --------------------------------------------- | -------------------------------- |
| master  | `ARCHITECTURE.md`                             | Top-level architecture authority |
| domain  | `docs/adr/`                                   | Implementation decisions          |
| feature | `docs/specs/`                                 | Implementation detail            |

## Related

- `[../prd/2026-03-15-governance-hub.md]`
- `[../specs/2026-03-15-metadata-spec.md]`
- `[../adr/0001-lazy-loading-rules.md]`
