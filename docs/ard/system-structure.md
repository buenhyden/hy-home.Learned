---
title: 'Global Architecture Reference Document (ARD)'
status: 'Approved'
date: '2026-03-14'
owner: 'buenhyden'
scope: 'master'
tags: ['ard', 'architecture']
layer: 'common'
---

# Global Architecture Reference Document (ARD)

> **Status**: Approved
> **Scope**: master
> **layer:** common
> **Related PRD**: `docs/prd/documentation-system-prd.md`

**Overview (KR):** 프로젝트의 폴더링 기반 문서 구조와 각 레이어별 아키텍처 원칙을 정의하는 전역 참조 문서입니다.

## Technical or Platform Baseline

The system uses a partitioned documentation strategy where files are grouped by intent (ADR, PRD, Spec) and nested within category folders.

## System Overview

### [Layer: Global] Knowledge Hub Architecture

Documentation is organized into:

- `docs/adr/`: Architecture Decision Records.
- `docs/ard/`: Architecture Reference Documents.
- `docs/prd/`: Product Requirements.
- `docs/specs/`: Technical Specifications.
- `docs/plans/`: Execution Plans.
- `docs/runbooks/`: Operational Procedures.
- `docs/operations/`: Incident and Postmortem records.

## Documentation Chain

- Upstream: [prd.md](../prd/documentation-system-prd.md)
- Related decisions: [adr.md](../adr/0001-documentation-restructuring.md)
- Downstream contracts: [specs.md](../specs/2026-03-14-documentation-spec.md)

---

_Last Updated: March 2026_
