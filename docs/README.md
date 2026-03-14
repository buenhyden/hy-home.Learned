# Documentation Hub (`docs/`)

This directory is the long-term, human-readable knowledge base for the `hy-home-learned` repository.

## Purpose

- Provide a stable navigation layer for all project documentation.
- Maintain separate contexts for requirements, architecture, implementation, and operations.
- Support lazy loading by providing indexed category documents.

## Knowledge Map (by Category)

- [ADRs](adr/0001-documentation-restructuring.md) for architecture decisions
- [ARDs](ard/system-structure.md) for system blueprints
- [PRDs](prd/documentation-system-prd.md) for product requirements
- [Specs](specs/2026-03-14-documentation-spec.md) for implementation contracts
- [Plans](plans/2026-03-14-restructure-plan.md) for execution records
- [Runbooks](runbooks/operational-procedures.md) for operational procedures
- [Operations](operations/README.md) for incident records
- [Agentic](agentic/README.md) for AI Agent instructions

## Documentation Rules

- **Metadata mandatory**: Each file must contain `Layer: <layer_name>` metadata at the top.
- **Flattened structure**: All individual documentation files live in this root `docs/` directory.
- **Templates**: Use matching templates in [../templates/](../templates/).
- **Links**: Keep links repository-relative.

---

_Last Updated: March 2026_
