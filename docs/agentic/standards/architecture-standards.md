# Architecture Standards

> **layer:** agentic
> **Status**: Active
> **Source**: Refactored from `.agent/rules/0100-Standards/0130-architecture-standard.md`

- **Role**: System Architect
- **Purpose**: Define standards for the high-level structural design and component interaction patterns.

## 1. Core Principles

- **[REQ-ARC-01] Documentation-First Blueprinting**: Every project MUST possess a root `ARCHITECTURE.md` file.
- **[REQ-ARC-02] Immutable Decision Tracking (ADR)**: Significant deviations MUST be documented as ADRs.
- **[REQ-ARC-03] Strict Directional Dependency**: Dependencies MUST flow in a single direction (e.g., Presentation -> Domain -> Data).

## 2. Structural Standards

- **[REQ-ARC-04] Modeling**: Use C4 Context/Container diagrams (Mermaid).
- **[REQ-ARC-08] Lifecycle**: ADRs MUST maintain an explicit status (Proposed, Accepted, Superceded).
- **[REQ-ARC-10] Hierarchy**: Codebase structure MUST align with project-wide defined hierarchy.

## 3. Mandatory Constraints

- **[BAN-ARC-01] Opaque Logic**: Avoid patterns that hide fundamental system flow or side-effects.
- **[BAN-ARC-02] Infrastructure Leakage**: Domain logic MUST NOT depend directly on infrastructure details.

## 4. Validation Criteria

- [ ] **[VAL-ARC-01]** `ARCHITECTURE.md` is present and valid.
- [ ] **[VAL-ARC-02]** High impact decisions have corresponding ADRs.
- [ ] **[VAL-ARC-03]** Zero circular dependencies between top-level modules.
