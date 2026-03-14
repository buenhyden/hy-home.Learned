---
title: 'ADR 0001: Folder-Based Documentation Hierarchy'
status: 'Accepted'
date: '2026-03-14'
authors: ['Antigravity']
deciders: ['buenhyden']
tags: ['adr', 'governance', 'documentation']
---

# ADR 0001: Folder-Based Documentation Hierarchy

- **Status:** Accepted
- **Date:** 2026-03-14
- **Scope:** master

**Overview (KR):** 프로젝트 문서 관리 체계를 파일 타입별 폴더 구조(docs/adr/, docs/prd/ 등)로 정립하고, 각 파일 내부에서 레이어별 메타데이터를 사용하여 관리하는 결정입니다.

## Context

The repository documentation required a clear hierarchy that balances category isolation with layer-centric organization. Previous attempts failed to strictly adhere to the project's markdown templates and structural requirements. A folder-per-type structure was chosen to support multiple records per category while maintaining a primary focus on functional layers.

## Decision

- Use a folder-based structure: `docs/<category>/`.
- Categories include: `adr`, `ard`, `prd`, `specs`, `plans`, `runbooks`, `operations`.
- Each file must follow the updated templates in `templates/`, including frontmatter and layer metadata.
- Internal categorization within files is done via functional layers (e.g., `common`, `architecture`, `infra`).

## Consequences

- **Positive**: High compatibility with repository templates and standards.
- **Positive**: Scalable structure that allows multiple files per category folder.
- **Consequence**: requires strict adherence to template formatting for tools and humans.

## Related

- `docs/prd/documentation-system-prd.md`
- `docs/specs/2026-03-14-documentation-spec.md`

---

_Last Updated: March 2026_
