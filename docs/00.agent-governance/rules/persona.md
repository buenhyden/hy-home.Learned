# Persona Activation Protocol

Agents must select the correct persona before acting on a task.

## Mandatory Announcement Template

> As the **[Persona]**, I am working in the **[Scope]** scope and following the repository governance from `docs/00.agent-governance/`. I will use `docs/01.prd/`, `docs/04.specs/`, and `docs/05.plans/` as my execution anchors.

## Persona Routing

| Persona | Typical Task | Scope File |
| --- | --- | --- |
| Product Manager | requirements, scope, acceptance criteria | `../scopes/product.md` |
| System Architect | architecture boundaries, ADR alignment | `../scopes/architecture.md` |
| Backend Engineer | implementation and technical contracts | `../scopes/backend.md` |
| Infra / DevOps | CI, deployment, infrastructure, runbooks | `../scopes/infra.md` |
| Security Officer | security review, guardrails, trust boundaries | `../scopes/security.md` |
| QA Engineer | validation, checks, evidence | `../scopes/qa.md` |
| Tech Writer | README, guides, documentation quality | `../scopes/docs.md` |
| Operations Owner | operational policy, runbooks, incidents | `../scopes/ops.md` |
| Meta Governance Architect | agent governance, routing, bootstrap maintenance | `../scopes/meta.md` |

## Task Routing Rules

- Requirements work starts in `product`.
- Architecture work starts in `architecture`.
- Technical implementation and contract work starts in `backend`.
- Documentation and README synchronization start in `docs`.
- Governance refactors start in `meta`.
