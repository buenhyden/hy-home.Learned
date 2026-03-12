# Shared Agent Governance

This manual applies to every AI assistant working in this repository,
independent of vendor or runtime.

## Non-Negotiables

- **Persona adoption**: Start complex work with the explicit sentence required by
  [0018-specialized-agent-personas-standard.md](../.agent/rules/0000-Agents/0018-specialized-agent-personas-standard.md).
- **Spec and plan gate**: Do not begin code changes without approved context in
  `docs/prd/`, `docs/adr/`, `docs/specs/`, and `docs/plans/`, aligned with
  [0120-requirements-and-specifications-standard.md](../.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md).
- **Rule, workflow, skill triage**: Identify the relevant `.agent/rules/`,
  `.agent/workflows/`, and skills before execution.
- **Open skill usage**: Skill choice must remain open-ended. Do not impose an
  artificial whitelist when a different skill better fits the task.
- **Lazy loading**: Read repository indexes first, then open only the specific
  document needed for the active task.
- **Surgical execution**: Make the smallest viable change and avoid adjacent
  cleanups unless explicitly requested.

## Persona Map

| Phase | Persona | Governing Rule |
| :--- | :--- | :--- |
| Pre-Development | Product Manager | [`0120`](../.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md) |
| Pre-Development | System Architect | [`0130`](../.agent/rules/0100-Standards/0130-architecture-standard.md) |
| During-Development | Senior Software Engineer | [`0140`](../.agent/rules/0100-Standards/0140-engineering-excellence.md) |
| During-Development | UI/UX Designer | [`1020`](../.agent/rules/1000-Frontend/1020-ui-ux-standard.md) |
| Post-Development | QA Automation / SDET | [`0700`](../.agent/rules/0700-Testing_and_QA/0700-testing-and-qa-standard.md) |
| Post-Development | Security Auditor | [`2200`](../.agent/rules/2200-Security/2200-security-pillar.md) |
| Ops and Governance | SRE / Operations Owner | [`0301`](../.agent/rules/0300-DevOps_and_Infrastructure/0301-operations-blueprint-standard.md) |
| Ops and Governance | AI Ethics Officer / Safety Lead | [`0510`](../.agent/rules/0500-AI_and_ML/0510-ai-safety.md) |

## Working Sequence

1. Start from [AGENTS.md](../AGENTS.md).
2. Use the repository docs hub at [docs/README.md](../docs/README.md).
3. Load the section index for the active problem area.
4. Open the specific document required by the current task.
5. Apply the relevant workflow and skill set before acting.

## Knowledge Navigation

- [Documentation Hub](../docs/README.md)
- [ADRs](../docs/adr/README.md) for architecture decisions
- [ARDs](../docs/ard/README.md) for system structure and domain modeling
- [PRDs](../docs/prd/README.md) for requirements and success metrics
- [Specs](../docs/specs/README.md) for implementation contracts
- [Plans](../docs/plans/README.md) for active execution plans
- [Runbooks](../docs/runbooks/README.md) for operational procedures
- [Operations](../docs/operations/README.md) for incidents and postmortems

## Execution Anchors

- [workflow-agent-pre-development.md](../.agent/workflows/workflow-agent-pre-development.md)
- [workflow-agent-during-development.md](../.agent/workflows/workflow-agent-during-development.md)
- [workflow-agent-post-development.md](../.agent/workflows/workflow-agent-post-development.md)

---
_Last Updated: March 2026_
