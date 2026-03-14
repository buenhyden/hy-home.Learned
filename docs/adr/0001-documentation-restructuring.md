# ADR 0001: Documentation Restructuring and Agentic Hub Centralization

- **Status:** Accepted
- **Date:** 2026-03-14
- **Scope:** master
- **layer:** agentic
- **Authors:** Antigravity

**Overview (KR):** 프로젝트 문서 구조를 폴더 기반 계층 구조로 재편하고, AI Agent 명령어를 `docs/agentic/`으로 중앙 집중화하며 lazy-loading trigger를 구현하기 위한 의사결정입니다.

## Context

The current repository structure has core documentation files in the root and fragmented agent instructions. To improve maintainability, AI agent precision, and documentation discoverability, a structured hierarchy and specialized instructions hub are required.

## Decision

- Adopt a folder-based documentation hierarchy under `docs/` (`ard/`, `adr/`, `prd/`, `specs/`, `plans/`, `runbooks/`, `operations/`).
- Centralize all detailed AI Agent instructions and standards in `docs/agentic/`.
- Transform `.agent/rules/` into lightweight "trigger" files that lazy-load deep context from `docs/agentic/`.
- Mandate `layer:` metadata in all documentation files for better context filtering.

## Consequences

- **Positive**: Increased AI reasoning precision due to smaller, focused context windows.
- **Positive**: Better documentation governance and traceability.
- **Trade-off**: Higher initial overhead to create and maintain mandated documents (ADR, ARD, etc.).

## Related

- `[../ard/0001-documentation-hierarchy.md]`
- `[../prd/0001-agentic-hub-refinement.md]`
- `[../specs/2026-03-14-lazy-loading-implementation.md]`
