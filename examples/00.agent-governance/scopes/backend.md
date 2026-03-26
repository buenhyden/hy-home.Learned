# Backend Layer Scope (March 2026)

`layer: backend`

This scope defines the technical constraints for the Backend Engineer persona.

## 1. Core Responsibilities

- **Stage 04 (Specs)**: Implement technical specs in `docs/04.specs/`. Use `spec.template.md`.
- **Stage 05 (Plans)**: Create implementation plans in `docs/05.plans/`. Use `plan.template.md`.
- **Contract-First**: Define machine-readable contracts in `contracts/` before any logic.

## 2. Standard Taxonomy

- **API Spec**: Use `api-spec.template.md` and `openapi.template.yaml`.
- **Data model**: Use `data-model.template.md` or `schema.template.graphql`.
- **Implementation**: MUST be grounded in `docs/04.specs/` and `docs/05.plans/`.

## 3. Required Metadata

```markdown
---
layer: backend
stage: 04
---
```

## 4. Skills Engagement

- `nodejs-backend-patterns`
- `postgresql-optimization`
- `api-design-principles`
- `fastapi-pro` (if Python)
