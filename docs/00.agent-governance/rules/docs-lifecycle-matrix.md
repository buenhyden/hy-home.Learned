# Docs Lifecycle Matrix (00~11)

This matrix unifies purpose, timing, ownership, inputs, outputs, templates, and done criteria for the numeric docs taxonomy.

| Stage | Purpose | Authoring Timing | Owner Persona | Input Docs | Output Docs | Template | Done Criteria |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 `agent-governance` | Agent routing, policy, provider notes | Before and during AI-agent execution model changes | Meta Governance Architect | `AGENTS.md`, `docs/README.md`, provider docs | Updated governance rules/scopes/providers | N/A (governance docs) | Routing order is valid, language policy enforced, provider chains valid |
| 01 `prd` | Product intent and acceptance criteria | Before architecture and implementation design | Product Manager | Problem statement, business goals | Requirement document | `../99.templates/prd.template.md` | Scope, non-goals, acceptance criteria, and success metrics are explicit |
| 02 `ard` | Architecture reference and system boundaries | After PRD, before detailed technical design | System Architect | PRD | Architecture reference | `../99.templates/ard.template.md` | Boundaries, quality attributes, and reference architecture are clear |
| 03 `adr` | Decision records for key architecture choices | When a significant architecture decision is made | System Architect | PRD, ARD, prior ADRs | Decision record | `../99.templates/adr.template.md` | Context, decision, alternatives, and consequences are explicit |
| 04 `specs` | Technical contracts and detailed design | After PRD/ARD/ADR and before implementation | Backend Engineer / System Architect | PRD, ARD, ADR | Spec package with contracts/tests design | `../99.templates/spec.template.md` (+ related templates) | Interfaces, data contracts, verification, and non-goals are explicit |
| 05 `plans` | Execution sequencing, risk control, rollout plan | After spec approval and before task execution | Product Manager / Tech Lead | PRD, Specs, ADR | Execution plan | `../99.templates/plan.template.md` | Phased execution, verification gates, and completion criteria are defined |
| 06 `tasks` | Task-level implementation/evidence tracking | During implementation and validation | Backend Engineer / QA Engineer | Plan, Spec | Task records and evidence | `../99.templates/task.template.md` | Each task has owner, validation evidence, and status |
| 07 `guides` | Human-facing usage and how-to documentation | When user/operator guidance is required | Tech Writer | Spec, Runbook, Operations | Guide docs | `../99.templates/guide.template.md` | Audience, prerequisites, steps, and linked references are complete |
| 08 `operations` | Operational policies and control standards | Before or alongside production operations | Operations Owner / Security Officer | Specs, compliance requirements | Operations policy | `../99.templates/operation.template.md` | Controls, policy boundaries, and exceptions are explicit |
| 09 `runbooks` | Executable operational procedures | When repeatable operational actions are needed | Operations Owner / Infra / DevOps | Operations policy, Specs | Runbook procedures | `../99.templates/runbook.template.md` | Preconditions, steps, validation, rollback, and escalation are complete |
| 10 `incidents` | Incident facts, timeline, mitigation record | During or immediately after incidents | Operations Owner / Incident Commander | Runbooks, live evidence | Incident report | `../99.templates/incident.template.md` | Impact, timeline, actions, evidence, and linked follow-ups are captured |
| 11 `postmortems` | Blameless root-cause analysis and prevention actions | After incident stabilization | Operations Owner / System Architect | Incident report, runbooks, specs | Postmortem analysis | `../99.templates/postmortem.template.md` | Root cause, contributing factors, and owned prevention actions are documented |

## Notes

- This matrix summarizes current stage README contracts.
- For template details, see `docs/99.templates/README.md`.
- For governance completion gates, see `quality-standards.md`.
