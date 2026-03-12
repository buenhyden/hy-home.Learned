# Shared Agent Governance

This manual applies to every AI assistant working in this repository, regardless
of model.

## Non-Negotiables

- **Persona adoption**: Start complex work with the explicit sentence required by
  [0018-specialized-agent-personas-standard.md](../.agent/rules/0000-Agents/0018-specialized-agent-personas-standard.md).
- **Spec and plan gate**: Do not begin code changes without approved context in
  `docs/prd/`, `docs/adr/`, `docs/specs/`, and `docs/plans/` as reinforced by
  [0120-requirements-and-specifications-standard.md](../.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md)
  and the implementation workflows.
- **Rule, workflow, skill triage**: Identify the relevant `.agent/rules/`,
  `.agent/workflows/`, and active skills before execution.
- **Lazy loading**: Read README or index documents first, then only the files
  needed for the active task.
- **Surgical execution**: Make the smallest viable change and avoid adjacent
  cleanups unless explicitly requested.

## Persona Map

| Phase | Persona | Governing Rule |
| :--- | :--- | :--- |
| Pre-Development | Product Manager | `0120-requirements-and-specifications-standard.md` |
| Pre-Development | System Architect | `0130-architecture-standard.md` |
| During-Development | Senior Developer | `0140-engineering-excellence.md` |
| During-Development | UI/UX Designer | `1020-ui-ux-standard.md` |
| Post-Development | QA Automation | `0700-testing-and-qa-standard.md` |
| Post-Development | Security Auditor | `2200-security-pillar.md` |
| Ops and Governance | SRE / DevOps | `0301-operations-blueprint-standard.md` |
| Ops and Governance | AI Safety Lead | `0510-ai-safety.md` |

## Knowledge Navigation

Open these documents in this order when you need project context:

- [ADRs](../docs/adr/README.md) for architecture decisions
- [ARDs](../docs/ard/README.md) for system structure and domain modeling
- [PRDs](../docs/prd/README.md) for requirements and success metrics
- [Specs](../docs/specs/) for implementation blueprints
- [Plans](../docs/plans/) for current task execution
- [Runbooks](../docs/runbooks/) for operational procedures in the current repo
- [Operations](../docs/operations/) for incidents and postmortems
- [Guides](../docs/guides/README.md) for phase-specific execution
- [Manuals](../docs/manuals/README.md) for project-specific working agreements

## Local Override Rules

- The documents in [docs/guides/](../docs/guides/README.md) override generic
  execution behavior when they define a more specific project rule.
- The documents in [docs/manuals/](../docs/manuals/README.md) override generic
  governance when they define team-specific working agreements.
- Use the collaboration guide for human/AI handoff conventions:
  [collaboration-guide.md](../docs/manuals/collaboration-guide.md).

## Execution Anchors

- [workflow-agent-pre-development.md](../.agent/workflows/workflow-agent-pre-development.md)
- [workflow-agent-during-development.md](../.agent/workflows/workflow-agent-during-development.md)
- [workflow-agent-post-development.md](../.agent/workflows/workflow-agent-post-development.md)

---
_Last Updated: March 2026_
