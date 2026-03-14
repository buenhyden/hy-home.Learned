---
title: 'Documentation Structure Specification'
status: 'Canonical'
version: '1.0'
owner: 'buenhyden'
scope: 'master'
prd_reference: '../prd/documentation-system-prd.md'
arch_reference: '../ard/system-structure.md'
tags: ['spec','implementation']
layer: 'common'
---

# Documentation Structure Specification

> **Status**: Canonical
> **Scope**: master
> **layer**: common
> **Related PRD**: `../prd/documentation-system-prd.md`
> **Related Architecture**: `../ard/system-structure.md`

**Overview (KR):** 폴더링 기반의 문서 구조를 구현하기 위한 파일 배치 규격, 메타데이터 표준 및 네비게이션 연결 방식을 정의하는 기술 명세입니다.

## Technical or Platform Baseline

- **Base Directory**: `docs/`
- **Sub-Directories**: `adr/`, `ard/`, `prd/`, `specs/`, `plans/`, `runbooks/`, `operations/`.
- **Instruction Hub**: `docs/agentic/`.

## Contracts

- **Frontmatter Contract**: Every file in these folders must include the YAML frontmatter defined in `templates/`.
- **Metadata Contract**: Callouts for Status, Scope, and Layer must be present H1.
- **Pathing Contract**: Cross-document links must use relative paths (e.g., `../prd/`).

## Verification

- [ ] `find docs -type d` shows all 7 core category folders.
- [ ] `docs/README.md` links point to folders or primary record files.

---

_Last Updated: March 2026_
