# Agent Governance Refactor Specification

## Overview (KR)

이 문서는 에이전트 거버넌스 리팩터링의 기술 설계와 구현 계약을 정의한다. 루트 entrypoint 파일, `docs/00.agent-governance/` 구조, README 동기화 규칙, 그리고 `.agent` 호환성 처리 방식을 명확히 한다.

## Strategic Boundaries & Non-goals

This spec owns the repository's governance entrypoints, the `docs/00.agent-governance/` structure, and the README synchronization rules that follow from the refactor. It does not own runtime implementation code, CI behavior changes, or any rewrite of existing written content under `docs/01~99/`.

## Related Inputs

- **PRD**: `[../../01.prd/2026-03-26-agent-governance-refactor.md]`
- **ARD**: `N/A`
- **Related ADRs**: `N/A`

## Contracts

- **Config Contract**: Root entry files remain small and provider-specific files remain modular.
- **Data / Interface Contract**: The active governance tree under `docs/00.agent-governance/` exposes only `rules/`, `scopes/`, `providers/`, and `memory/`.
- **Governance Contract**: Human-facing root guidance is Korean; active AI-agent governance documents are English.

## Core Design

- **Component Boundary**:
  - `AGENTS.md`: shared bootstrap
  - `CLAUDE.md`: Claude shim
  - `GEMINI.md`: Gemini shim
  - `docs/00.agent-governance/rules/`: universal routing and standards
  - `docs/00.agent-governance/scopes/`: task-layer rules
  - `docs/00.agent-governance/providers/`: provider notes
  - `docs/00.agent-governance/memory/`: optional memory templates
- **Key Dependencies**:
  - `docs/README.md`
  - `pyproject.toml`
  - `.github/workflows/ci.yml`
  - `.agent/` compatibility files
- **Tech Stack**: Markdown documentation managed in a Python `uv` repository

## Data Modeling & Storage Strategy

- **Schema / Entity Strategy**: Not applicable beyond the fixed documentation tree and ownership map.
- **Migration / Transition Plan**:
  - Create new routing files first.
  - Replace root shims next.
  - Move to example-aligned tree.
  - Delete obsolete governance directories last.

## Interfaces & Data Structures

### File Ownership Map

- `AGENTS.md`: universal bootstrap and repository taxonomy
- `CLAUDE.md`: imports `AGENTS.md` and `providers/claude.md`
- `GEMINI.md`: imports `AGENTS.md` and `providers/gemini.md`
- `README.md`: Korean repository guide that reflects the final post-refactor state
- `docs/00.agent-governance/README.md`: English governance hub README reflecting the final post-refactor state

## API Contract (If Applicable)

Not applicable.

## Agent Role & IO Contract (If Applicable)

- **Agent Role**: Governance refactor executor
- **Inputs**:
  - Current repository structure
  - Existing governance files
  - Example structure
  - Official provider guidance
- **Outputs**:
  - Refactored root entry files
  - Example-aligned governance tree
  - Updated README files
  - New PRD and Spec
- **Success Definition**: The final structure is consistent, minimal, example-aligned, and validated.

## Tools & Tool Contract (If Applicable)

- **Tool List**: file reading, patch-based editing, shell-based validation
- **Permission Boundary**: modify only the files explicitly in scope
- **Failure Handling**: stop if validation repeatedly fails or if the final structure diverges from the example alignment

## Prompt / Policy Contract (If Applicable)

- **System / Instruction Contract**: Root files bootstrap the repository and route the agent to narrower scopes.
- **Policy Constraints**:
  - No edits to existing written content in `docs/01~99/`
  - No Korean text in `docs/00.agent-governance/`
  - README files must reflect the completed structure, not a transitional state
- **Versioning Rule**: Root governance files must carry `2026-03-26` as the effective refresh date

## Memory & Context Strategy (If Applicable)

- **Short-term Context**: `AGENTS.md` -> `rules/bootstrap.md` -> `rules/persona.md` -> matching scope/provider file
- **Long-term Memory**: optional `memory/` templates only
- **Retrieval Boundary**: no broad load of unrelated scopes or legacy directories

## Guardrails (If Applicable)

- **Input Guardrails**: Do not derive repository reality from stale governance files when `pyproject.toml` or directory structure disagree.
- **Output Guardrails**: Do not leave stale paths or deleted directories mentioned in active docs.
- **Blocked Conditions**: stop if example alignment requires editing existing written content under `docs/01~99/`
- **Escalation Rule**: escalate only if a required mutation would violate the immutable-docs constraint

## Evaluation (If Applicable)

- **Eval Types**:
  - structural scan
  - stale path scan
  - language scan
  - root file line-budget scan
- **Metrics**:
  - zero stale path matches in active governance files
  - zero Korean matches in `docs/00.agent-governance/`
  - expected file tree shape
- **Datasets / Fixtures**: current repository tree and example governance tree
- **How to Run**: shell-based validation commands captured in the Verification section

## Edge Cases & Error Handling

- **Legacy Compatibility**: `.agent/` remains available, but only core compatibility entrypoints are refreshed in this pass.
- **README Drift**: if structure changes late in the refactor, both README files must be updated again before final validation.

## Failure Modes & Fallback / Human Escalation

- **Failure Mode**: new governance tree is correct but README still describes removed folders
- **Fallback**: update README files before final validation
- **Human Escalation**: only if a requested deletion would require changing immutable docs under `docs/01~99/`

## Verification

```bash
find docs/00.agent-governance -maxdepth 2 -type f | sort
rg -n "docs/(prd|adr|specs|plans|runbooks|operations)|docs/agentic|templates/|file:///|\\.agent/" AGENTS.md GEMINI.md CLAUDE.md docs/00.agent-governance
rg -n "[가-힣]" docs/00.agent-governance
wc -l AGENTS.md GEMINI.md CLAUDE.md
```

## Success Criteria & Verification Plan

- **VAL-SPC-001**: `docs/00.agent-governance/` top-level matches the example alignment exactly.
- **VAL-SPC-002**: Root entry files are minimal and provider import chains are valid.
- **VAL-SPC-003**: Root `README.md` and governance `README.md` both reflect the final completed structure.
- **VAL-SPC-004**: Active governance files contain no stale paths.

## Related Documents

- **Plan**: `[../../05.plans/2026-03-26-agent-governance-refactor-plan.md]`
- **Tasks**: `N/A`
- **Runbook**: `N/A`
