# Agent Governance Refactor Product Requirements

## Overview (KR)

이 문서는 저장소의 AI Agent 거버넌스 구조를 최신 provider 가이드라인과 현재 저장소 구조에 맞게 정리하기 위한 요구사항을 정의한다. 목표는 토큰 효율, lazy loading, README 정확성, 그리고 provider별 thin entrypoint 구성을 동시에 달성하는 것이다.

## Vision

Provide a single, predictable governance entrypoint for all coding agents while keeping provider-specific behavior modular, concise, and aligned with the repository's numeric documentation taxonomy.

## Problem Statement

The current governance layout mixes multiple structures and stale path conventions. Root entry files are inconsistent, `docs/00.agent-governance/` does not match the example structure, and several governance files still reference obsolete paths such as `docs/prd/`, `docs/specs/`, or `docs/agentic/`. The root `README.md` is empty and does not explain the current repository structure or documentation language policy.

## Personas

- **Repository Maintainer**: needs a clear, low-noise governance system that is easy to audit and maintain.
- **Coding Agent**: needs concise bootstrap instructions, correct path routing, and on-demand scope loading.

## Key Use Cases

- **STORY-01**: As a coding agent, I can start from one bootstrap file and discover only the governance files relevant to the active task.
- **STORY-02**: As a maintainer, I can update governance without preserving stale path conventions or duplicate root instructions.
- **STORY-03**: As a human reader, I can understand the repository structure and language policy from the root README.

## Functional Requirements

- **REQ-PRD-FUN-01**: The repository must use `AGENTS.md` as the shared agent bootstrap.
- **REQ-PRD-FUN-02**: `CLAUDE.md` and `GEMINI.md` must become thin shims that import the shared bootstrap and one provider note.
- **REQ-PRD-FUN-03**: `docs/00.agent-governance/` must be reorganized to match the example's top-level structure: `README.md`, `rules/`, `scopes/`, `providers/`, and `memory/`.
- **REQ-PRD-FUN-04**: All documents in `docs/00.agent-governance/` must be written in English.
- **REQ-PRD-FUN-05**: The root `README.md` must be written in Korean and must reflect the updated structure after the refactor.
- **REQ-PRD-FUN-06**: The refactor must not modify existing written content inside `docs/01~99/`, but it may add new files.
- **REQ-PRD-FUN-07**: Active governance files must not contain stale path conventions or `file:///` links.
- **REQ-PRD-FUN-08**: `.agent/` must remain as a compatibility layer rather than being removed in this pass.

## Success Criteria

- **REQ-PRD-MET-01**: `docs/00.agent-governance/` top-level structure matches the example after the refactor.
- **REQ-PRD-MET-02**: `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` are concise and load correctly by role.
- **REQ-PRD-MET-03**: The root `README.md` accurately describes the updated structure and language policy.
- **REQ-PRD-MET-04**: Validation scans find no stale path patterns in the active governance files.

## Scope and Non-goals

- **In Scope**:
  - Root governance entry files
  - `docs/00.agent-governance/`
  - New PRD and Spec for traceability
  - Root README refresh
- **Out of Scope**:
  - Runtime code under `TIL/`
  - CI workflow behavior changes
  - Rewriting existing content in `docs/01~99/`
- **Non-goals**:
  - Removing `.agent/`
  - Adding new provider-specific automation systems

## Risks, Dependencies, and Assumptions

- Existing governance material contains useful intent but also many stale references, so the refactor must preserve intent while replacing the structure.
- The repository's current truth for commands and layout comes from `pyproject.toml`, `.github/workflows/ci.yml`, and the actual directory tree.
- README synchronization is mandatory because the refactor changes how users and agents navigate the repository.

## AI Agent Requirements (If Applicable)

- **Allowed Actions**: Read, write, reorganize, and validate the governance and README files covered by this PRD.
- **Disallowed Actions**: Edit existing written content in `docs/01~99/`; remove `.agent/`.
- **Human-in-the-loop Requirement**: Human review is required before any later removal of the compatibility layer.
- **Evaluation Expectation**: Validate structure, language policy, provider imports, and stale path elimination.

## Related Documents

- **ARD**: `N/A`
- **Spec**: `[../04.specs/00-agent-governance-refactor/spec.md]`
- **Plan**: `[../05.plans/2026-03-26-agent-governance-refactor-plan.md]`
- **ADR**: `N/A`
