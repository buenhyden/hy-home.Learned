# Architecture Layer Scope (March 2026)

`layer: architecture`

This scope defines the technical constraints and standards for the System Architect persona.

## 1. Core Responsibilities

- **Stage 02 (ARD)**: Maintain the **Architecture Reference Document** in `docs/02.ard/`. Use `ard.template.md`.
- **Stage 03 (ADR)**: Record all technical decisions in **Architecture Decision Records** in `docs/03.adr/`. Use `adr.template.md`.
- **Cross-Stage Alignment**: Ensure all technical specifications in `docs/04.specs/` align with the approved ARD/ADR.

## 2. Standard Taxonomy

- **ARD**: High-level blueprint. MUST contain Mermaid C4-Context/Container diagrams.
- **ADR**: Focused decision log. Numbered sequentially (`001-initial-choice.md`).
- **Templates**: Reference `docs/99.templates/ard.template.md` and `adr.template.md`.

## 3. Required Metadata

All architecture documents MUST include:

```markdown
---
layer: architecture
stage: [02|03|04]
---
```

## 4. Skills Engagement

The agent MUST use the following skills for architecture tasks:

- `c4-architecture`
- `architecture-decision-records`
- `mermaid-diagrams`
- `software-architecture`
