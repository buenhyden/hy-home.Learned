---
title: 'Documentation Restructuring Plan'
status: 'In Progress'
date: '2026-03-14'
owner: 'buenhyden'
scope: 'master'
tags: ['implementation', 'planning']
stack: 'documentation'
layer: 'common'
---

# Documentation Restructuring Plan

> **Status**: In Progress
> **Scope**: master
> **layer**: common

**Overview (KR):** 문서 관리의 일관성과 템플릿 준수를 위해 기존 루트 파일 방식에서 폴더 기반 계층 구조로 전환하고, 모든 기존 기록을 해당 위치로 이전하는 실행 계획입니다.

## 1. Context and Problem Statement

Fragmented documentation and incorrect structural interpretation required a pivot back to folder-based isolation as specified in updated repository templates.

## 2. Execution Steps

- [x] Create category directories (`adr/`, `ard/`, `prd/`, `specs/`, `plans/`, `runbooks/`, `operations/`).
- [x] Re-format and move content into template-compliant files within folders.
- [x] Update central navigation in `docs/README.md`.
- [x] Cleanup obsolete root files and directories.

## References

- `[../prd/documentation-system-prd.md]`
- `[../specs/2026-03-14-documentation-spec.md]`
- `[../ard/0001-documentation-hub-architecture.md]`

---

_Last Updated: March 2026_
