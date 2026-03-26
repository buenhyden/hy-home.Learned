# AI Agent Standards (March 2026)

This document defines the universal technical standards for all AI Agents working on **Project-Template**.

## 1. Token Optimization & JIT Context Loading

- **Thin Root Policy**: Keep `AGENTS.md`, `GEMINI.md`, and `CLAUDE.md` under 200 tokens. Use `@` pointer-based modularity.
- **JIT Sequence**:
  1. Load `rules/bootstrap.md`.
  2. Identify Task Layer via file discovery.
  3. Load layer-specific scope from `scopes/`.
- **No Redundancy**: Do not duplicate instructions. Use references to shared rule files.

## 2. Documentation Standards

- **Protocol Compliance**: ALL documentation MUST follow the [Documentation Protocol](documentation-protocol.md).
- **JIT README Sync**: Implementation-level `README.md` files MUST be updated JIT after any functional changes or task completions (`Stage 06`).

## 3. Architecture & Design Governance

- **Architecture First Policy**: Before implementing any feature (`Stage 05+`), agents MUST verify the existence of a corresponding **ARD (Stage 02)** and **ADR (Stage 03)** in `docs/`. If missing, the agent MUST flag this as a risk.
- **Contract-First Policy**: All API and interface designs MUST be documented as **Machine-Readable Contracts** (OpenAPI, Proto, GraphQL) in a `contracts/` subdirectory within the feature folder (`docs/04.specs/<feature>/contracts/`) before implementation begins.
- **Stage-Gate Compliance**: Documentation must follow the `01-11` taxonomy. Implementation code must NOT be written until `Stage 04 (Specs)` is finalized and verified.

## 4. Response Protocol

- **Language (KR)**: (요청에 대한 답변은 한글로 한다) - All user-facing communication MUST be in Korean. Use the `humanizer` skill for natural phrasing.
- **Technical Tasks (EN)**: All technical governance (`docs/00.agent-governance/`) and technical specs (`docs/04.specs/`) MUST be written in **English** for global AI interoperability.

## 5. Verification Standards (Stage 05)

- **Validation First**: Every Implementation Plan (Stage 05) MUST include an explicit Verification Plan with pass/fail criteria.
- **Evidence-Based**: Agents MUST provide evidence of verification (test logs, screenshots, or recordings) in the final walkthrough.
- **Ladder of Verification**: Start with unit tests, followed by integration tests, and finally E2E/manual verification.

## 6. Incident & Risk Protocol (Stage 10)

- **Risk First**: When an incident occurs, the priority is risk mitigation and service restoration. Documentation (Stage 11) follows restoration.
- **Blameless Culture**: Postmortems (Stage 11) MUST focus on systemic improvements, not individual agent or human errors.
