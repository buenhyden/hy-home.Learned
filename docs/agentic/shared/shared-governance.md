# Shared Agent Governance

> **layer:** agentic

This manual applies to every AI assistant working in this repository,
independent of vendor or runtime.

## Non-Negotiables

- **Persona adoption**: Start complex work with the explicit sentence required by
  [0018-specialized-agent-personas-standard.md](../.agent/rules/0000-Agents/0018-specialized-agent-personas-standard.md).
- **Spec and plan gate**: Do not begin code changes without approved context in
  `docs/prd/`, `docs/adr/`, `docs/specs/`, and `docs/plans/`, aligned with
  [Requirements Standard](../docs/agentic/pillar.md).
- **Rule, workflow, skill triage**: Identify the relevant `.agent/rules/`,
  `.agent/workflows/`, and skills before execution.
- **Open skill usage**: Skill choice must remain open-ended. Do not impose an
  artificial whitelist when a different skill better fits the task.
- **Lazy loading**: Read repository indexes first, then open only the specific
  document needed for the active task.
- **Surgical execution**: Make the smallest viable change and avoid adjacent
  cleanups unless explicitly requested.

## Persona Map

| Phase              | Persona                         | Governing Rule                                                                                 |
| :----------------- | :------------------------------ | :--------------------------------------------------------------------------------------------- |
| Pre-Development    | Product Manager                 | [PRDs](../docs/prd/)                  |
| Pre-Development    | System Architect                | [ADRs](../docs/adr/)                  |
| During-Development | Senior Software Engineer        | [Specs](../docs/specs/)              |
| During-Development | UI/UX Designer                  | [UI/UX Standard](../docs/agentic/README.md) |
| Post-Development   | QA Automation / SDET            | [Plans](../docs/plans/)              |
| Post-Development   | Security Auditor                | [Security Standard](../docs/agentic/pillar.md) |
| Ops and Governance | SRE / Operations Owner          | [Runbooks](../docs/runbooks/)        |
| Ops and Governance | AI Ethics Officer / Safety Lead | [Safety Standard](../docs/agentic/management.md) |

## Working Sequence

1. Start from [AGENTS.md](../AGENTS.md).
2. Use the repository docs hub at [docs/README.md](../docs/README.md).
3. Load the section index for the active problem area.
4. Open the specific document required by the current task.
5. Apply the relevant workflow and skill set before acting.

## Knowledge Navigation

- [Documentation Hub](../docs/README.md)
- [ADRs](../../adr/) for architecture decisions
- [ARDs](../../ard/) for system structure and domain modeling
- [PRDs](../../prd/) for requirements and success metrics
- [Specs](../../specs/) for implementation contracts
- [Plans](../../plans/) for active execution plans
- [Runbooks](../../runbooks/) for operational procedures
- [Operations](../../operations/) for incidents and postmortems
- [Agentic](../README.md) for AI instructions and governance

## Execution Anchors

- [workflow-agent-pre-development.md](../.agent/workflows/workflow-agent-pre-development.md)
- [workflow-agent-during-development.md](../.agent/workflows/workflow-agent-during-development.md)
- [workflow-agent-post-development.md](../.agent/workflows/workflow-agent-post-development.md)

---

_Last Updated: March 2026_
