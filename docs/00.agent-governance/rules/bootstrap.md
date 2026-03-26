# Agent Bootstrap Governance

This file is the universal governance entrypoint for repository work.

## Core Rules

- Start from `docs/README.md` and load only the relevant index or target file.
- Anchor implementation and documentation changes to `docs/01.prd/` or `docs/04.specs/`.
- Track execution in `docs/05.plans/`.
- Activate a task-appropriate persona and scope before acting.

## Numeric Documentation Taxonomy

| Stage | Path | Purpose |
| --- | --- | --- |
| 00 | `docs/00.agent-governance/` | AI-agent governance and provider notes |
| 01 | `docs/01.prd/` | Product requirements |
| 02 | `docs/02.ard/` | Architecture reference documents |
| 03 | `docs/03.adr/` | Architecture decision records |
| 04 | `docs/04.specs/` | Technical specifications |
| 05 | `docs/05.plans/` | Execution plans |
| 06 | `docs/06.tasks/` | Task tracking |
| 07 | `docs/07.guides/` | Guides |
| 08 | `docs/08.operations/` | Operational policy |
| 09 | `docs/09.runbooks/` | Runbooks |
| 10 | `docs/10.incidents/` | Incident records |
| 11 | `docs/11.postmortems/` | Postmortems |
| 90 | `docs/90.references/` | Reference material |
| 99 | `docs/99.templates/` | Templates |

## Lazy-Loading Sequence

1. Load the relevant docs index.
2. Read the matching PRD or Spec for the task.
3. Load `rules/persona.md`.
4. Load the matching scope file.
5. Load provider notes only when runtime behavior matters.

## Working Flow

`01.prd` -> `02.ard` / `03.adr` -> `04.specs` -> `05.plans` -> `06.tasks` -> `07~11`
