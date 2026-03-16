# ADR 0002: Path Pluralization Standard

> **Status:** Accepted
> **Date:** 2026-03-15
> **Scope:** master
> **layer:** common

**Overview (KR):** 프로젝트 문서 디렉토리 경로를 복수형(plural)으로 표준화하여 일관성을 확보하고 탐색 효율성을 높이는 결정입니다.

## Context

The repository previously had a mix of singular and plural directory names for documentation (e.g., `docs/adr/` vs `docs/prd/` but `docs/specs/` and `docs/plans/`). This inconsistency leads to confusion for both humans and AI agents when creating or referencing artifacts.

## Decision

- Standardize all documentation subdirectories within `docs/` to use plural names.
- Specifically:
  - `docs/plans/` (enforce over `docs/plan/`)
  - `docs/specs/`
  - `docs/runbooks/`
  - `docs/operations/incidents/`
  - `docs/operations/postmortems/`
- All cross-references and internal documentation links must be updated to reflect these plural paths.

## Consequences

- Improved consistency across the repository.
- Reliable path prediction for AI agents.
- Clearer hierarchy for heavy documentation sets.

## Related

- `[../ard/0001-documentation-hub-architecture.md]`
- `[../plans/2026-03-15-refactor-execution.md]`
