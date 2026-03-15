# Metadata and Trigger Specification

> **Status**: Canonical
> **Scope**: master
> **layer:** agentic

**Overview (KR):** 문서 파일의 `layer:` 메타데이터 형식과 AI Agent 명령어를 위한 단축 트리거(Short-form trigger)의 기술적 형식을 정의합니다.

## Technical Baseline

All Markdown documents in the `docs/` hierarchy MUST include a `layer:` metadata tag in the first 5 lines.

## Contracts

- **Metadata Contract**:
  - Key: `layer:`
  - Values: `common | architecture | backend | frontend | infra | mobile | product | qa | security | agentic`
  - Format: `> **layer:** <value>` or in frontmatter.

- **Trigger Contract**:
  - File: `.agent/rules/NNNN-name.md`
  - Body: MUST contain an H2 `# Trigger` and a link to the detail layer in `docs/agentic/`.

## Verification

```bash
# Verify metadata
grep -r "layer:" docs/
# Verify triggers
grep -r "docs/agentic/" .agent/rules/
```
