# Documentation Hub (`docs/`)

This directory contains long-term, human-readable project documentation used across planning, design, and reference delivery.

## 1. Necessity and Purpose

This directory acts as the stable knowledge base for the `hy-home-learned` ecosystem. It isolates product/design knowledge ("Why" and "What") from executable logic, operational scripts, and AI automation logic.

- **Human Developers**: Primary reference for understanding overarching system constraints.
- **AI Agents**: Source of truth for planning and design validation via **Lazy Loading**.

## 2. Knowledge Map (Lazy Loading)

Documents created here MUST use their respective templates from the `templates/` folder and adhere to [**AGENTS.md**](../AGENTS.md) navigation rules.

- [**ADRs (Architecture Decisions)**](adr/README.md) — Rationale for technical choices.
- [**ARDs (Architecture References)**](ard/README.md) — Domain models and structural diagrams.
- [**PRDs (Product Requirements)**](prd/README.md) — Business goals and user stories.
- [**Guides (Lifecycle)**](guides/README.md) — Procedures for Pre/During/Post-Dev phases.
- [**Manuals (Non-Technical)**](manuals/README.md) — Collaboration and operations agreements.

## 3. Explicit Boundaries & Anti-Patterns

1. **NO RUNBOOKS ALLOWED**: All playbooks and incident response guides MUST go in the root `/runbooks/` directory.
2. **NO SPECS ALLOWED**: All feature-specific implementation blueprints and plans belong in `/specs/` or `/docs/plans/`.
3. **NO AI WORKFLOWS ALLOWED**: Behavioral guidelines and prompts belong strictly in `.agent/workflows/`.
4. **TEMPLATE MANDATORY**: New ADRs, ARDs, and PRDs MUST be generated from the `templates/` directory.
5. **LOCALE ADHERENCE**: Follow [**Korean Overview Protocol**](.agent/rules/2500-Localization/) for all major docs.

---
_Last Updated: March 2026_
