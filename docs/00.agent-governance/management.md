# Agentic Instruction Management

> **layer:** agentic

> **Layer**: agentic
> **Status**: Active

This document guides how AI Agent instructions are structured, versioned, and loaded in this repository.

## Management Standards

1. **Centralized in `docs/agentic/`**: All long-form instructions, reasoning frameworks, and persona definitions must reside here. This is the authoritative source for AI Agent governance.
2. **Purpose-Driven Skill Selection**: Instructions must NOT restrict agents to specific skill whitelists. Instead, agents are guided to select the most appropriate skill for the objective.
3. **Lazy Loading Protocol**: Short-form trigger rules in `.agent/rules/` MUST link to these long-form documents for deep context. Agents should never act on triggers alone without loading the authorized detail layer.
4. **Historical Preservation**: Legacy instructions that are being refactored must be analyzed to ensure critical reasoning patterns and project-specific knowledge are preserved.

## Refinement Workflow

- When a new agent capability is added, update the [README.md](README.md) index.
- Ensure all persona updates are reflected in [personas.md](personas.md).
- Maintain [pillar.md](pillar.md) as the absolute source of truth for reasoning quality.

## Collaboration & Conflict Resolution

1. **Protocol-Driven Handoffs**:
    - **Planner**: PRD (`docs/prd/`) -> Spec (`docs/specs/`).
    - **Coder**: Implements EXACTLY as specified. Stops and asks if edge cases are undocumented.
    - **DevOps**: Generates/updates runbooks (`docs/runbooks/`).
2. **Conflict Resolution (Hallucinations)**:
    - If a conflict occurs, human intervention should focus on adjusting the specification or adding constraints to `docs/guides/`.
    - Agents must be re-pointed to the specific markdown line disregarded.
3. **Rule Evolution**: Standard rules live in `.agent/rules/`, but project-specific deep context stays in `docs/agentic/`.

---
_Last Updated: March 2026_
