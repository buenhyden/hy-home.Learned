# Agent Governance Refactor Plan

> Use this template for `docs/05.plans/YYYY-MM-DD-<feature>.md`.
>
> Rules:
>
> - Every active plan must include explicit verification criteria.
> - Plan explains execution order, risk control, and rollout strategy.

---

# Agent Governance Refactor Plan

## Overview (KR)

이 문서는 루트 `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, 그리고 `docs/00.agent-governance/`를 2026년 3월 기준 공식 가이드라인과 현재 저장소 상태에 맞게 재구성하기 위한 실행 계획서다. 목표는 토큰 사용량을 줄이면서도, AI Agent가 필요한 규칙만 지연 로딩하고, 작업별 persona와 rule을 정확히 활성화할 수 있는 구조를 만드는 것이다.

## Context

이번 리포지토리는 다음 제약 아래에서 정리되어야 한다.

- 기존 `docs/01~99/`의 작성된 내용은 수정하지 않는다.
- `docs/00.agent-governance/`는 `examples/00.agent-governance/`의 구조를 따라야 한다.
- `docs/00.agent-governance/` 내부 문서는 모두 영어로 유지한다.
- 루트 `README.md`는 한국어로 작성하고, `docs/` 내 문서 언어 원칙을 명시해야 한다.
- 현재 저장소는 `uv` 기반 Python 프로젝트이며, 실제 구조는 `TIL/`, `tests/`, `.github/`, `.agent/`, `docs/` 중심이다.

현재 상태에서 확인된 핵심 문제는 다음과 같다.

- 루트 `README.md`가 비어 있어 저장소 진입 문서 역할을 하지 못한다.
- `docs/00.agent-governance/`가 example 구조와 다르게 `shared/`, `instructions/`, `standards/` 중심으로 분화되어 있다.
- 다수 문서가 현재 숫자형 docs taxonomy가 아닌 레거시 경로(`docs/prd`, `docs/specs`, `docs/agentic`, `templates/`)를 참조한다.
- `.agent/` 기반 레거시 규칙과 `docs/00.agent-governance/`가 중복되며, 어느 쪽이 정본인지 불명확하다.
- 루트 entrypoint 파일인 `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`는 provider별 최신 권장 패턴 대비 과도하게 독자 구조를 갖고 있고, 상호 재사용이 약하다.

## Research Summary

### 1. Official Guidance Snapshot (as checked on 2026-03-26)

| Topic | Official Guidance | Repository Implication |
| --- | --- | --- |
| `AGENTS.md` | OpenAI Codex guidance says `AGENTS.md` scope is the directory tree rooted at the containing folder, deeper nested files take precedence, direct system/developer/user instructions override it, and any programmatic checks named there must be run even for documentation changes. The `agents.md` project describes it as a predictable "README for agents". | Keep root `AGENTS.md` minimal and universal. Put only rules that truly apply repo-wide. Delegate detail to `docs/00.agent-governance/` and nested governance fragments. |
| `CLAUDE.md` | Anthropic Claude Code docs say Claude reads `CLAUDE.md`, not `AGENTS.md`; `CLAUDE.md` may import `@AGENTS.md`. Project `CLAUDE.md` should stay specific, concise, and ideally under 200 lines. Large instruction sets should be split via imports or `.claude/rules/`, and subdirectory files load on demand. | Rebuild `CLAUDE.md` as a thin shim: import `AGENTS.md`, then load only Claude-specific provider notes. Reserve heavy detail for modular fragments. |
| `GEMINI.md` | Gemini CLI docs say `GEMINI.md` files form hierarchical instructional memory across global, project/ancestor, and subdirectory files. `/memory show`, `/memory list`, and `/memory refresh` expose the active context. `@file` imports support modularization, and `context.fileName` can optionally include alternative names such as `AGENTS.md`. | Rebuild `GEMINI.md` as a thin shim that imports shared governance. Do not rely on user-specific `context.fileName` settings for correctness; make the repo work with default `GEMINI.md` behavior. |

### 2. Refactor Direction

| Area | Current Problem | Refactor Direction |
| --- | --- | --- |
| Root files | Entry files duplicate structure and hard-code repo-specific links in inconsistent ways. | Make `AGENTS.md` the canonical cross-agent bootstrap. Make `CLAUDE.md` and `GEMINI.md` provider shims that import it plus one provider file. |
| `docs/00.agent-governance/` | Structure does not match example and mixes triggers, deep standards, and provider overlays without a clear dispatch model. | Normalize to `README.md`, `rules/`, `scopes/`, `providers/`, and optional `memory/`. |
| Lazy loading | Current docs use broad "load these shared files" behavior but still point to large, overlapping documents. | Move to strict router-style documents: bootstrap -> persona -> scope -> provider. |
| Traceability | Governance docs mention traceability but still point to obsolete paths. | Align every active reference to `docs/01.prd/` through `docs/11.postmortems/` numeric taxonomy. |
| Persona/rule activation | Personas exist but are not wired cleanly to docs stages and example-style scopes. | Add one explicit persona activation rule and stage-aware scope routing file set. |

## Goals & In-Scope

- **Goals**:
  - Normalize `docs/00.agent-governance/` to the example structure while preserving repository-specific reality.
  - Make `AGENTS.md`, `GEMINI.md`, and `CLAUDE.md` token-efficient entry files.
  - Enforce lazy loading through router documents instead of monolithic overlays.
  - Make provider-specific behavior explicit without duplicating shared rules.
  - Add a Korean root `README.md` that explains the documentation map and language strategy.

- **In Scope**:
  - `AGENTS.md`
  - `GEMINI.md`
  - `CLAUDE.md`
  - `README.md`
  - `docs/00.agent-governance/**`
  - New meta-governance artifacts required for traceability in `docs/01.prd/`, `docs/04.specs/`, and `docs/05.plans/`

## Non-Goals & Out-of-Scope

- **Non-goals**:
  - Editing existing written content in `docs/01~99/`
  - Removing the legacy `.agent/` system in the first refactor pass
  - Changing runtime code under `TIL/`, `tests/`, or `.github/`

- **Out of Scope**:
  - Broad repo-wide documentation rewrite outside root `README.md`
  - Replacing provider tooling behavior with custom wrappers
  - Building a new automation system for governance generation in this pass

## Target Structure

`docs/00.agent-governance/` should converge to the following shape.

```text
docs/00.agent-governance/
├── README.md
├── rules/
│   ├── bootstrap.md
│   ├── standards.md
│   ├── persona.md
│   ├── git-workflow.md
│   ├── documentation-protocol.md
│   └── quality-standards.md
├── scopes/
│   ├── architecture.md
│   ├── backend.md
│   ├── docs.md
│   ├── infra.md
│   ├── meta.md
│   ├── ops.md
│   ├── product.md
│   ├── qa.md
│   └── security.md
├── providers/
│   ├── claude.md
│   └── gemini.md
└── memory/
    ├── README.md
    └── template.md
```

## File Strategy

### Root Entry Files

| File | Strategy |
| --- | --- |
| `AGENTS.md` | Keep under roughly 50 to 80 lines. Only universal repository bootstrap, taxonomy, language policy, persona/rule dispatch, and mandatory verification policy. |
| `CLAUDE.md` | Convert to a thin shim using `@AGENTS.md` and `@docs/00.agent-governance/providers/claude.md`. Claude-specific notes only. |
| `GEMINI.md` | Convert to a thin shim using `@AGENTS.md` and `@docs/00.agent-governance/providers/gemini.md`. Gemini-specific notes only. |
| `README.md` | Write in Korean. Explain repository purpose, docs lifecycle, and the rule that AI-agent-operational docs are English while human-facing docs are Korean. |

### Governance Files

| Area | Strategy |
| --- | --- |
| `rules/bootstrap.md` | One true dispatch entry for numeric docs taxonomy and lazy-loading sequence. |
| `rules/persona.md` | One announcement template and one persona-to-stage/scope matrix. |
| `rules/documentation-protocol.md` | Root README and docs language rules, template usage, and synchronization rules. |
| `rules/standards.md` | Cross-cutting standards only. Eliminate duplicate trigger wrappers. |
| `rules/quality-standards.md` | Verification, evidence, and documentation update gates. |
| `scopes/*.md` | Task-layer detail only. Keep each file short and role-specific. |
| `providers/*.md` | Provider-specific loader semantics, not repository-wide rules. |

## Work Breakdown

| Task | Description | Files / Docs Affected | Target REQ | Validation Criteria |
| --- | --- | --- | --- | --- |
| PLN-001 | Create a new PRD for governance refactor without editing existing `docs/01.prd/` content. | `docs/01.prd/2026-03-26-agent-governance-refactor.md` | GOV-REQ-001 | PRD exists and states scope, constraints, language policy, and non-goals. |
| PLN-002 | Create a new spec for the refactor so all documentation changes have a formal contract. | `docs/04.specs/00-agent-governance-refactor/spec.md` | GOV-REQ-002 | Spec defines target structure, file responsibilities, loader semantics, and verification. |
| PLN-003 | Rewrite root `AGENTS.md` into a universal bootstrap aligned with the latest AGENTS.md guidance. | `AGENTS.md` | GOV-REQ-003 | File is minimal, repo-wide, conflict-free, and contains no obsolete path references. |
| PLN-004 | Rewrite `CLAUDE.md` into a thin provider shim that imports `AGENTS.md` and the Claude provider notes. | `CLAUDE.md`, `docs/00.agent-governance/providers/claude.md` | GOV-REQ-004 | Claude root file is short, uses `@AGENTS.md`, and all Claude-specific guidance is moved out of root. |
| PLN-005 | Rewrite `GEMINI.md` into a thin provider shim that imports `AGENTS.md` and the Gemini provider notes. | `GEMINI.md`, `docs/00.agent-governance/providers/gemini.md` | GOV-REQ-005 | Gemini root file is short, uses `@` imports correctly, and does not depend on custom local settings. |
| PLN-006 | Rebuild `docs/00.agent-governance/README.md` to match the example structure and explain JIT loading. | `docs/00.agent-governance/README.md` | GOV-REQ-006 | README matches example structure, references only current numeric docs paths, and stays in English. |
| PLN-007 | Collapse current `shared/`, `standards/`, and `instructions/` content into `rules/`, `scopes/`, and `providers/`. | `docs/00.agent-governance/**` | GOV-REQ-007 | No active governance doc remains outside the example-aligned structure except optional `memory/`. |
| PLN-008 | Define persona routing and task-to-scope dispatch so agents must select the right persona and rules per task. | `docs/00.agent-governance/rules/persona.md`, `docs/00.agent-governance/scopes/*.md` | GOV-REQ-008 | Persona file includes stage mapping and scope activation rules for product, architecture, backend, docs, qa, ops, security, and meta tasks. |
| PLN-009 | Add Korean root README guidance for the docs language split and repository navigation. | `README.md` | GOV-REQ-009 | Root README is Korean and clearly says AI-facing governance/spec docs are English, human-facing docs are Korean. |
| PLN-010 | Remove or quarantine obsolete references to legacy paths from active governance docs. | `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `docs/00.agent-governance/**` | GOV-REQ-010 | No active file contains stale links such as `docs/prd`, `docs/specs`, `docs/agentic`, `templates/`, or `file:///...`. |
| PLN-011 | Preserve `.agent/` as a compatibility layer and point it to the new governance source of truth instead of expanding it. | `.agent/**`, `docs/00.agent-governance/**` | GOV-REQ-011 | Legacy layer is explicitly marked compatibility-only and no longer acts as the primary governance source. |
| PLN-012 | Run final structural, language, and link validation across the refactored files. | Root files and `docs/00.agent-governance/**` | GOV-REQ-012 | All verification commands in this plan pass. |

## Verification Plan

| ID | Level | Description | Command / How to Run | Pass Criteria |
| --- | --- | --- | --- | --- |
| VAL-PLN-001 | Structural | Verify `docs/00.agent-governance/` matches the example-aligned top-level shape. | `find docs/00.agent-governance -maxdepth 2 -type f | sort` | Output contains only `README.md`, `rules/`, `scopes/`, `providers/`, and optional `memory/` files expected by the plan. |
| VAL-PLN-002 | Reference | Scan for obsolete path patterns in active governance files. | `rg -n "docs/(prd|adr|specs|plans|runbooks|operations)|docs/agentic|templates/|file:///|\\.agent/" AGENTS.md GEMINI.md CLAUDE.md docs/00.agent-governance` | No stale path appears in active guidance except explicitly labeled legacy compatibility notes. |
| VAL-PLN-003 | Language | Ensure `docs/00.agent-governance/` remains English-only. | `rg -n "[가-힣]" docs/00.agent-governance` | No matches. |
| VAL-PLN-004 | Language | Ensure root `README.md` is Korean and contains docs language policy. | Manual review of `README.md` | Korean narrative exists and explicitly states the English/Korean document split. |
| VAL-PLN-005 | Token Budget | Check that root entry files stay thin. | `wc -l AGENTS.md GEMINI.md CLAUDE.md` | `AGENTS.md` stays under 80 lines, `GEMINI.md` and `CLAUDE.md` stay under 40 lines each unless a justified exception is documented. |
| VAL-PLN-006 | Provider Semantics | Verify Claude shim imports `AGENTS.md` and Gemini shim uses valid `@` imports. | Manual review | Import syntax is correct for each provider and relative paths resolve from the containing file. |
| VAL-PLN-007 | Repo Reality | Confirm toolchain and command references match the current workspace. | Manual review against `pyproject.toml`, `.github/workflows/ci.yml`, and actual directories | Commands and paths reflect `uv`, Python 3.13, `TIL/`, `tests/`, `.github/`, and current CI behavior. |

## Risks & Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Over-refactoring the governance tree into too many small files | Medium | Keep only the example-required folders and avoid splitting by topic beyond rules/scopes/providers. |
| Breaking provider behavior with incorrect import semantics | High | Validate `CLAUDE.md` and `GEMINI.md` separately against their official import models before merge. |
| Leaving stale legacy links in newly refactored files | High | Run `VAL-PLN-002` before completion and block merge on any unresolved legacy reference. |
| Creating a governance model that ignores current repository reality | High | Treat `pyproject.toml`, `.github/workflows/ci.yml`, directory tree, and current docs indices as the source of truth. |
| Drifting away from `examples/00.agent-governance/` over time | Medium | Reuse the example’s top-level structure exactly and record any intentional deviations in the new spec. |

## Agent Rollout & Evaluation Gates (If Applicable)

- **Offline Eval Gate**:
  - `VAL-PLN-001` through `VAL-PLN-007` must pass before merge.
- **Sandbox / Canary Rollout**:
  - Validate with one Claude session and one Gemini session in the refactor branch before treating the new layout as canonical.
- **Human Approval Gate**:
  - Human review is required before replacing current root entry files and before deleting or archiving legacy governance fragments.
- **Rollback Trigger**:
  - Roll back if either provider fails to load the intended context chain, or if active docs still depend on stale paths after refactor.
- **Prompt / Model Promotion Criteria**:
  - Promotion is allowed only when both providers can derive the right task scope from root entrypoints without broad repository ingestion.

## Completion Criteria

- [ ] New PRD and Spec for this governance refactor are created without modifying existing written content in `docs/01~99/`
- [ ] `docs/00.agent-governance/` matches the example-aligned structure
- [ ] `AGENTS.md`, `GEMINI.md`, and `CLAUDE.md` are thin entrypoints
- [ ] Root `README.md` is Korean and documents the language split for `docs/`
- [ ] Verification passed
- [ ] Required docs updated

## Related Documents

- **PRD**: `TBD - create docs/01.prd/2026-03-26-agent-governance-refactor.md during execution`
- **ARD**: `N/A for initial documentation-only planning unless structural architecture changes require one`
- **Spec**: `TBD - create docs/04.specs/00-agent-governance-refactor/spec.md during execution`
- **ADR**: `Optional - add only if the team decides to formally preserve the dual-layer model (.agent compatibility + docs/00 canonical governance)`

## External References

- OpenAI, "Introducing Codex" AGENTS.md spec section: <https://openai.com/index/introducing-codex/>
- agents.md open format repository: <https://github.com/agentsmd/agents.md>
- Anthropic Claude Code docs, "How Claude remembers your project": <https://code.claude.com/docs/en/memory>
- Gemini CLI docs, "Provide Context with GEMINI.md Files": <https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html>
- Gemini CLI docs, configuration reference: <https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html>
