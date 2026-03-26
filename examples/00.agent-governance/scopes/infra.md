# Infrastructure Layer Scope (March 2026)

`layer: infra`

This scope defines the technical constraints for the Infra/DevOps Miner persona.

## 1. Core Responsibilities

- **Stage 08 (Operations)**: Document environment configs in `docs/08.operations/`. Use `operation.template.md`.
- **Stage 09 (Runbooks)**: Maintain operational procedures in `docs/09.runbooks/`. Use `runbook.template.md`.
- **IaC Standards**: All Infrastructure as Code (Terraform/Docker) MUST be grounded in Stage 08 documentation.

## 2. Standard Taxonomy

- **Inventory**: Resource mapping in `docs/08.operations/inventory.md`.
- **Incident Response**: Use `docs/10.incidents/` and `incident.template.md` for active issues.
- **Post-mortems**: Mandatory for Stage 11. Use `postmortem.template.md`.

## 3. Required Metadata

```markdown
---
layer: infra
stage: 08
---
```

## 4. Skills Engagement

- `terraform-specialist`
- `kubernetes-architect`
- `docker-expert`
- `deployment-procedures`
