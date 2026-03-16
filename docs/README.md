# Documentation Hub (`docs/`)

This directory is the long-term, human-readable knowledge base for the `hy-home-learned` repository.

## Purpose

- Provide a stable navigation layer for all project documentation.
- Maintain separate contexts for requirements, architecture, implementation, and operations.
- Support lazy loading by providing indexed category documents.

## Knowledge Map (by Category)

- [ADRs](adr/README.md) for architecture decisions
- [ARDs](ard/README.md) for system blueprints
- [PRDs](prd/README.md) for product requirements
- [Specs](specs/README.md) for implementation contracts
- [Plans](plans/README.md) for execution records
- [Guides](guides/README.md) for usage instructions
- [Manuals](manuals/README.md) for detailed references
- [Runbooks](runbooks/README.md) for operational procedures
- [Operations](operations/README.md) for incident records
- [Agentic](agentic/README.md) for AI Agent instructions

## Documentation Rules

- **Metadata mandatory**: Each file must contain `layer: <layer_name>` metadata in frontmatter or callouts.
- **Folder-based structure**: All documentation files are categorized into subdirectories (`adr/`, `prd/`, etc.).
- **Plural naming**: Directory names must be plural (e.g., `docs/plans/` not `docs/plan/`).
- **Templates**: Always use the predefined [templates](../templates/).
- **Links**: Relative paths must be used for cross-references.

---

_Last Updated: March 2026_
