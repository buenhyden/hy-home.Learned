# Agent Bootstrap Governance

This file is the universal routing entrypoint for repository governance.

## Core Rules

- Start from `docs/README.md` and load only the minimum required files.
- Anchor every change to `docs/01.prd/` or `docs/04.specs/`.
- Track execution evidence in `docs/05.plans/`.
- Complete `pre-task-checklist.md` before implementation work.
- Select persona and scope before code or documentation mutations.

## Numeric Taxonomy

| Stage | Path | Purpose |
| --- | --- | --- |
| 00 | `docs/00.agent-governance/` | AI-agent governance |
| 01 | `docs/01.prd/` | Product requirements |
| 02 | `docs/02.ard/` | Architecture references |
| 03 | `docs/03.adr/` | Architecture decisions |
| 04 | `docs/04.specs/` | Technical contracts |
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

1. `docs/README.md`
2. Relevant PRD or Spec
3. `rules/pre-task-checklist.md`
4. `rules/persona.md`
5. Matching `scopes/*.md`
6. Matching `providers/*.md` only when needed

## Mandatory Gates

- Before edits: run checklist sections in `pre-task-checklist.md`.
- Before completion: run `path-validation.md` and `quality-standards.md`.

## Working Flow

`01.prd -> 02.ard/03.adr -> 04.specs -> 05.plans -> 06.tasks -> 07~11`
