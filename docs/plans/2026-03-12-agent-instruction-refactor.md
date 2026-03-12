# Agent Instruction Refactor Plan

> **Status**: Completed
> **Scope**: historical
> **Related PRD**: `N/A`
> **Related Architecture**: `[../ard/README.md](../ard/README.md)`
> **Decision Record**: `N/A`

**Overview (KR):** 이 계획은 루트 agent entrypoint와 `.claude` 공유 매뉴얼, 그리고 `docs/` 인덱스 체계를 실제 저장소 구조에 맞게 재정렬하기 위해 작성되었다. 구현 결과는 import 기반 runtime entrypoint, 복구된 lazy-loading 문서 체계, 그리고 정리된 README navigation으로 수렴한다.

## Context & Introduction

The repository had already started moving agent guidance into `.claude/`, but
the active instruction chain still referenced removed legacy documentation
paths. The `docs/` indexes also drifted away from the actual repository
layout, which broke the lazy-loading contract for ADRs, ARDs, PRDs, Specs,
Plans, Runbooks, and Operations records.

This plan captured the required refactor and now serves as the historical
record of what was implemented.

## Tasks

| Task | Description | Files Affected | Validation Criteria |
| ---- | ----------- | -------------- | ------------------- |
| TASK-001 | Refactor root instruction entrypoints | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | Root files follow the new runtime and navigation contract |
| TASK-002 | Rewrite shared `.claude` manuals | `.claude/README.md`, `.claude/shared-governance.md`, `.claude/claude-code.md`, `.claude/gemini-models.md` | Shared docs contain only valid paths and current governance structure |
| TASK-003 | Rebuild docs lazy-loading indexes | `docs/README.md`, `docs/adr/README.md`, `docs/ard/README.md`, `docs/prd/README.md`, `docs/specs/README.md`, `docs/plans/README.md`, `docs/runbooks/README.md`, `docs/operations/README.md` | Each document family has a valid index and template reference |
| TASK-004 | Repair top-level repository navigation | `README.md` | Broken documentation links are removed or replaced |
| TASK-005 | Record the implemented architecture | `docs/plans/2026-03-12-agent-instruction-refactor.md` | Historical plan reflects the final contract and verification |

## Implemented Contract

### Root Entry Points

- [AGENTS.md](../../AGENTS.md) remains the vendor-neutral open-format entrypoint.
- [CLAUDE.md](../../CLAUDE.md) is now a thin runtime entrypoint that imports:
  - [`.claude/shared-governance.md`](../../.claude/shared-governance.md)
  - [`.claude/claude-code.md`](../../.claude/claude-code.md)
- [GEMINI.md](../../GEMINI.md) is now a thin runtime entrypoint that imports:
  - [`.claude/shared-governance.md`](../../.claude/shared-governance.md)
  - [`.claude/gemini-models.md`](../../.claude/gemini-models.md)

### Shared Governance

- [`.claude/shared-governance.md`](../../.claude/shared-governance.md) now
  owns persona adoption, spec/plan gate language, rule/workflow/skill triage,
  and the repository lazy-loading sequence.
- The shared manuals no longer reference removed legacy documentation paths.

### Docs Navigation

- [docs/README.md](../README.md) is now the single docs hub.
- Section indexes now exist for:
  - [ADRs](../adr/README.md)
  - [ARDs](../ard/README.md)
  - [PRDs](../prd/README.md)
  - [Specs](../specs/README.md)
  - [Plans](README.md)
  - [Runbooks](../runbooks/README.md)
  - [Operations](../operations/README.md)

## Verification

- `[VAL-001]` Run a relative-link check across the root instruction files,
  `.claude/*.md`, docs hubs, and this plan file.
- `[VAL-002]` Run `rg` for stale path leakage covering removed legacy docs
  paths, old template subdirectories, and obsolete top-level rule links.
- `[VAL-003]` Confirm that `docs/specs/README.md`, `docs/plans/README.md`,
  `docs/runbooks/README.md`, and `docs/operations/README.md` exist.

## Outcome

- Root instruction files are concise and role-correct.
- `.claude/` is the authoritative shared instruction source.
- The docs hub and section indexes match the actual repository structure.
- The old broken references are removed from the active instruction chain.

## References

- [AGENTS.md](../../AGENTS.md)
- [CLAUDE.md](../../CLAUDE.md)
- [GEMINI.md](../../GEMINI.md)
- [`.claude/README.md`](../../.claude/README.md)
- [docs/README.md](../README.md)
