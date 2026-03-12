# Root Instruction Entrypoint Refinement Plan

> **Status**: Completed
> **Scope**: domain
> **Related PRD**: `N/A`
> **Related Spec**: `N/A`
> **Related Historical Plan**: `[2026-03-12-agent-instruction-refactor.md](2026-03-12-agent-instruction-refactor.md)`

**Overview (KR):** 이 계획은 이미 얇아진 루트 agent entrypoint를 한 번 더 정리해, `AGENTS.md`에는 모든 에이전트가 공통으로 필요한 실행 정보만 남기고 `CLAUDE.md`, `GEMINI.md`는 공유 매뉴얼을 가리키는 최소 runtime 진입점으로 더 일관되게 다듬기 위해 작성되었다.

## Context & Introduction

The repository already completed the larger March 12, 2026 instruction-system
refactor. This follow-up plan captures a smaller quality pass focused only on
the three root entrypoints. The goal is to preserve progressive disclosure
while improving universal command discoverability and making root navigation
more consistent across vendor-neutral and model-specific files.

## Tasks

| Task | Description | Files Affected | Validation Criteria |
| ---- | ----------- | -------------- | ------------------- |
| TASK-001 | Add a minimal universal quick-reference block to the vendor-neutral root guide | `AGENTS.md` | Root file stays concise and documents the non-obvious repository command surface |
| TASK-002 | Tighten Claude runtime entrypoint wording and shared-manual navigation | `CLAUDE.md` | Claude root remains import-first and points clearly to the shared manuals and repo map |
| TASK-003 | Tighten Gemini runtime entrypoint wording and shared-manual navigation | `GEMINI.md` | Gemini root remains import-first and points clearly to the shared manuals and repo map |
| TASK-004 | Index and verify this refinement pass | `docs/plans/README.md`, `docs/plans/2026-03-12-root-instruction-entrypoint-refinement.md` | Plan index is current and root-file links resolve |

## Verification

- `[VAL-001]` Run `sed -n` on `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` to confirm the final root contract is concise and internally consistent.
- `[VAL-002]` Run `rg -n "\\]\\((docs/README.md|AGENTS.md|\\.claude/README.md|\\.claude/shared-governance.md|\\.claude/claude-code.md|\\.claude/gemini-models.md)\\)" AGENTS.md CLAUDE.md GEMINI.md` to verify expected internal links remain present.
- `[VAL-003]` Run `git diff -- AGENTS.md CLAUDE.md GEMINI.md docs/plans/README.md docs/plans/2026-03-12-root-instruction-entrypoint-refinement.md` and confirm the scope is limited to the planned files.

## References

- `[../../AGENTS.md](../../AGENTS.md)`
- `[../../CLAUDE.md](../../CLAUDE.md)`
- `[../../GEMINI.md](../../GEMINI.md)`
- `[../../.claude/README.md](../../.claude/README.md)`
- `[../../.claude/shared-governance.md](../../.claude/shared-governance.md)`
- `[2026-03-12-agent-instruction-refactor.md](2026-03-12-agent-instruction-refactor.md)`
