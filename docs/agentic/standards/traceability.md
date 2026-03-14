# Traceability Standards

> **layer:** agentic
> **Status**: Active
> **Source**: Refactored from `.agent/rules/0100-Standards/0113-impl-traceability.md`

- **Role**: Quality Engineer
- **Purpose**: Enforce a clear documentation chain from requirements to implementation.

## 1. Traceability Chain

Every code change MUST be traceable via the following chain:

1. **PRD** (`docs/prd/`): The "Why" and business value.
2. **ADR/ARD** (`docs/adr/`, `docs/ard/`): The architectural decision and system blueprint.
3. **Spec** (`docs/specs/`): The technical contract and API definition.
4. **Plan** (`docs/plans/`): The step-by-step execution strategy.
5. **Implementation**: The actual code reflecting the previous documents.

## 2. Linking Requirements

- **Commits**: MUST reference the specific task ID or tracking number if available.
- **PRs**: MUST link to the corresponding PRD/Spec/Plan.
- **Rules**: Every mandatory rule or standard MUST have a unique ID (e.g., `[REQ-TRA-01]`).

## 3. Validation Criteria

- [ ] Every non-trivial PR has a linked Plan.
- [ ] Major features have an accompanying PRD.
- [ ] Architectural shifts have an Accepted ADR.
