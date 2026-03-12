# Product Requirements Documents (PRD)

This directory contains Product Requirements Documents that define the "What" and "Why" of product features in the `hy-home-learned` ecosystem.

## 1. Role in Documentation Hierarchy

PRDs are the starting point for the **Spec-Driven Development** (SDD) workflow. They capture business goals and user needs.

- **Next Step**: [**Architecture Decisions (ADR)**](../adr/) or [**Implementation Specs**](../../specs/).
- **Mapping**: Adheres to [**Requirements Standards**](../../.agent/rules/0120-requirements-and-specifications-standard.md).

## 2. Navigation Protocol (Lazy Loading)

AI Agents MUST follow the **Lazy Loading** pattern defined in [**AGENTS.md**](../../AGENTS.md):

1. Use this `README.md` to identify the relevant feature or domain epic.
2. Load only the specific PRD file required (e.g., `prd/auth-system.md`).

## 3. Reference Standards

Documents here MUST contain:

- **Vision**: Clear outcome-based goal statement.
- **Measurable Metrics**: Quantifiable success criteria (KPIs).
- **User Stories (GWT)**: Acceptance criteria in Given-When-Then format.
- **Out of Scope**: Explicit boundaries for the implementation phase.

## 4. Index of Requirements

| Feature / Epic | Title | Status | Target Version |
| :--- | :--- | :--- | :--- |
| - | _No PRDs yet_ | - | - |

---
_Last Updated: March 2026_

## Success Metrics

Define quantifiable and measurable success criteria as mandated by `[REQ-SPT-01] Explicit Success Metric Grounding`:

| Metric Type   | Example                        |
| ------------- | ------------------------------ |
| **Business**  | Increase conversion by 5%      |
| **User**      | Reduce time-to-complete by 30% |

## Relationship to Other Documents

```text
[User Need]
      ↓
docs/prd/ (What - Product Requirements)
      ↓
docs/ard/ (How - Architecture Requirements)
      ↓
specs/ (Implementation Specifications)
```

## PRD to Spec Workflow

1. **Planner Agent** creates PRD in `docs/prd/`, adhering to `.agent/rules/0120-requirements-and-specifications-standard.md`.
2. **Human** reviews and approves PRD.
3. **Planner Agent** generates spec in `specs/`.
4. **Reviewer Agent** validates specs against the PRD and formatting rules, ensuring GWT testability before implementation begins.
5. **Coder Agents** implement based on spec.

## AI Agent Guidelines

When working with PRDs:

1. **Use template**: Always use `templates/product/prd-template.md`
2. **Be specific**: Define quantifiable success metrics (No vague terms like "fast" without an explicit baseline).
3. **Include acceptance criteria**: Every feature needs testable criteria
4. **Link to specs**: After approval, create corresponding `specs/[feature]-spec.md`

## Index of PRDs

| Document | Feature       | Status | Last Updated |
| -------- | ------------- | ------ | ------------ |
| -        | _No PRDs yet_ | -      | -            |

> Add entries to this index as PRDs are created.
