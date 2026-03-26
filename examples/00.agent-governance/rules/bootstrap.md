# Agent Bootstrap Governance (March 2026)

> [!NOTE]
> **Project-Template**: A spec-driven repository. All work MUST be anchored to `docs/01.prd/` and `docs/04.specs/`.

This document is the universal entry point for all AI Agents. It enforces **Spec-Driven Development (SD)** and JIT metadata routing.

## 1. Core Principles

- **Spec-Anchored**: All work MUST be grounded in `docs/01.prd/` and `docs/04.specs/`.
- [Documentation Protocol](documentation-protocol.md): Standardized README and metadata requirements (March 2026).
- **Secondary Rules**: Refer to [AI Agent Standards](standards.md) and [Git Workflow](git-workflow.md).
- **Lazy Loading**: Load only this global governance initially; load layer-specific detail JIT via `docs/00.agent-governance/scopes/`.

## 2. Mandatory Taxonomy (Stage-Gate 01-11)

| Stage | Path | Purpose | SSoT |
| :--- | :--- | :--- | :--- |
| **00** | `docs/00.agent-governance/` | AI Agent Governance & Scopes (English Only) | Governance Rules |
| **01** | `docs/01.prd/` | Product Requirements & Intent | PRD |
| **02** | `docs/02.ard/` | Architecture Reference Documents | ARD |
| **03** | `docs/03.adr/` | Architectural Decision Records | ADR |
| **04** | `docs/04.specs/` | Technical Specifications (SSoT) | Specs |
| **05** | `docs/05.plans/` | Implementation & Validation Plans | Plan |
| **06** | `docs/06.tasks/` | Granular Task & Progress Tracking | task.md |
| **07** | `docs/07.guides/` | Operational & Developer Guides | Guide |
| **08** | `docs/08.operations/` | Monitoring & Environment State | Ops State |
| **09** | `docs/09.runbooks/` | Incident Response Procedures | Runbook |
| **10** | `docs/10.incidents/` | Live Incident Tracking | Incident List |
| **11** | `docs/11.postmortems/` | Retrospectives & Lessons Learned | Postmortem |
| **90** | `docs/90.references/` | Static References & Assets | Assets |
| **99** | `docs/99.templates/` | Markdown Templates | Templates |

## 3. Identity Protocol (Persona Activation)

Before starting, identify the target **Layer** via `grep -r "layer: <name>" docs/`. Load the corresponding scope from `docs/00.agent-governance/scopes/<layer>.md` and activate your persona.

Refer to [Agent Persona Protocol](persona.md) for mandatory announcement templates and persona-to-layer mapping.
