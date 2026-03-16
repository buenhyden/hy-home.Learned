---
title: 'Global Documentation Hub Architecture (ARD)'
status: 'Approved'
date: '2026-03-16'
owner: 'buenhyden'
scope: 'master'
tags: ['ard', 'architecture', 'governance']
layer: 'common'
---

# ARD 0001: Global Documentation Hub Architecture

> **Status:** Approved
> **Date:** 2026-03-16
> **Scope:** master
> **layer:** common

**Overview (KR):** 프로젝트의 폴더링 기반 문서 계층 구조, 메타데이터 표준, 그리고 AI 에이전트의 상황별 지침 로딩(Lazy-loading) 아키텍처를 정의하는 단일 진실 공급원(SSoT) 문서입니다.

## 1. Technical Baseline

The system leverages a partitioned documentation strategy to maintain high reasoning precision for AI agents and clear navigation for human maintainers.

### 1.1 Directory Hierarchy

Documentation is strictly organized into functional categories:

- `docs/adr/`: Architecture Decision Records (Chronological records of key choices).
- `docs/ard/`: Architecture Reference Documents (State of the system/domain).
- `docs/prd/`: Product Requirements Documents (Intent and problem space).
- `docs/specs/`: Technical Specifications (Technical contracts and implementation details).
- `docs/plans/`: Execution and Implementation Plans (Phased task ledgers).
- `docs/runbooks/`: Operational and Maintenance Runbooks (SOPs).
- `docs/operations/`: Operational records including `incidents/` and `postmortems/`.
- `docs/agentic/`: Definitive AI Agent instruction layers and hub.

## 2. Component Architecture

### 2.1 Context Loading Strategy (Lazy Loading)

To prevent context bloat, the system implements a **Trigger-to-Hub** model:

1. **Root Triggers**: Files in `.agent/rules/` contain minimal pointers.
2. **Deep Layers**: Detailed instructions residing in `docs/agentic/` are pulled only when the task intent requires them.

### 2.2 Metadata Standard

Every markdown artifact MUST include the `layer:` metadata to facilitate agentic filtering.

- **Values**: `common | architecture | backend | frontend | infra | mobile | product | qa | security | agentic`
- **Format**: `> **layer:** <value>` or YAML frontmatter.

## 3. Boundaries & Ownership

- **Owns**: Structural integrity of the `docs/` tree, cross-link contracts, and template adherence.
- **Consumes**: Requirements from Governance Hub PRD and Decision Records.
- **Primary Artifacts**: `docs/`, `templates/`.

## 4. Documentation Chain

The flow of authority follows:
`PRD` (Intent) -> `ARD` (Structure/State) -> `ADR` (Decision) -> `Spec` (Contract) -> `Plan` (Execution).

## Related

- `[../prd/2026-03-15-governance-hub.md]`
- `[../specs/2026-03-14-documentation-spec.md]`
- `[../adr/0001-documentation-restructuring.md]`
- `[../adr/0003-lazy-loading-rules.md]`
- `[../runbooks/documentation-maintenance.md]`
- `[../operations/postmortems/2026-03-14-cleanup-postmortem.md]`

---

_Last Updated: March 2026_
