# Metadata Hardening Specification

- **Status**: Canonical
- **Scope**: master
- **layer:** common
- **Related PRD**: `[../prd/2026-03-15-governance-hub.md]`
- **Related Architecture**: `[../ard/2026-03-15-documentation-structure.md]`

**Overview (KR):** 모든 프로젝트 문서에 `layer:` 메타데이터를 강제하고, 해당 값이 가질 수 있는 허용 범위를 정의하는 기술 명세입니다.

## Technical or Platform Baseline

All artifacts within this repository must be categorized by a functional layer to facilitate agent routing and context filtering.

## Contracts

- **Metadata Key**: `layer:`
- **Required Value Set**:
  - `common`: Cross-cutting or introductory content (e.g., READM, ADR, ARD).
  - `architecture`: System design and high-level structure.
  - `backend`: Server-side logic and APIs.
  - `frontend`: Web/Client interfaces.
  - `infra`: CI/CD, deployment, and cloud configuration.
  - `mobile`: Native application code.
  - `product`: Requirements and business logic.
  - `qa`: Test plans and verification logic.
  - `security`: Security policies and audits.
  - `agentic`: AI Agent instructions and governance.

- **Placement Contract**:
  - For Markdown: In a block quote at the top of the file: `> **layer:** <value>`.
  - Alternatively, in YAML frontmatter: `layer: <value>`.

## Verification

```bash
# Verify layer metadata presence in root markdown files
grep -r "layer:" *.md
# Verify layer metadata in docs/
grep -r "layer:" docs/
```

## Related Documents

- `[../ard/2026-03-15-documentation-structure.md]`
- `[../prd/2026-03-15-governance-hub.md]`
