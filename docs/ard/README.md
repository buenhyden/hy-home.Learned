# Architecture Reference Documents (ARD)

This directory stores the structural reference documents for the repository.
ARDs explain how the system is shaped, which boundaries exist, and how major
domains connect.

## Role In The Documentation Chain

- Upstream: [PRDs](../prd/README.md)
- Related decisions: [ADRs](../adr/README.md)
- Downstream contracts: [Specs](../specs/README.md)
- Governing rule:
  [0130-architecture-standard.md](../../.agent/rules/0100-Standards/0130-architecture-standard.md)

## Lazy Loading

1. Use this index to find the relevant system or domain.
2. Open only the ARD that matches the active task.
3. Follow links from that ARD to the related ADR, PRD, Spec, or Plan.

## Authoring Rules

- Use the [ARD Template](../../templates/ard-template.md).
- Keep ARDs architectural. File-level implementation detail belongs in a Spec.
- Link to the governing ADRs and downstream implementation documents when they
  exist.

## Index

| System / Domain | Title         | Status | Last Updated |
| --------------- | ------------- | ------ | ------------ |
| -               | _No ARDs yet_ | -      | -            |

> Add entries to this index as ARDs are created.

---

_Last Updated: March 2026_
