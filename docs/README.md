# Documentation Hub (`docs/`)

This directory is the long-term, human-readable knowledge base for the
`hy-home-learned` repository.

## Purpose

- Give humans and agents a stable navigation layer before they open individual
  documents.
- Separate requirements, architecture, implementation contracts, execution
  plans, and operational records.
- Support lazy loading by making each document family discoverable through a
  small index file first.

## Knowledge Map

- [ADRs](adr/README.md) for architecture decisions
- [ARDs](ard/README.md) for system structure and domain boundaries
- [PRDs](prd/README.md) for requirements and success criteria
- [Specs](specs/README.md) for implementation contracts
- [Plans](plans/README.md) for active execution plans
- [Runbooks](runbooks/README.md) for operational procedures
- [Operations](operations/README.md) for incidents and postmortems

## Lazy Loading Protocol

1. Start from this hub.
2. Open the relevant section index.
3. Read only the specific document needed for the active task.
4. Return to the index when you need a different document family.

## Documentation Rules

- Use the matching template in [../templates/](../templates/) when creating a
  new document.
- Keep links repository-relative.
- Keep index files short and specific.
- Do not treat this directory as a dumping ground for ad-hoc notes or agent
  prompts.

## Template Map

- [ADR Template](../templates/adr-template.md)
- [ARD Template](../templates/ard-template.md)
- [PRD Template](../templates/prd-template.md)
- [Spec Template](../templates/spec-template.md)
- [Plan Template](../templates/plan-template.md)
- [Runbook Template](../templates/runbook-template.md)
- [Incident Template](../templates/incident-template.md)

---
_Last Updated: March 2026_
