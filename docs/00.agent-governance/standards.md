# Agentic Reasoning Standards

> **layer:** agentic
> **Status:** Active Detail layer

## 1. 9-Step Execution Framework (Detail)

1. **Logical Dependencies**: Analyze prerequisites and reorder operations.
2. **Risk Assessment**: Identify consequences and mitigate side effects.
3. **Abductive Reasoning**: Generate and prioritize multiple hypotheses.
4. **Outcome Evaluation**: Pivot the plan based on tool results.
5. **Information Availability**: Exhaust all data sources before acting.
6. **Precision & Grounding**: Quote exact code or logs.
7. **Completeness**: Ensure 100% adherence to constraints.
8. **Persistence**: Retry transient failures intelligently.
9. **Final Inhibition**: Last cognitive pause before critical execution.

## 3. Project-Level Architectural Law

- **Spec-Driven Targets**: All implementation MUST be driven by a spec in `docs/specs/`. Hallucinations are mitigated by sticking to approved specs.
- **Template Integrity**: All artifacts MUST use `templates/` to ensure structural consistency for future AI tasks.
- **Boundary Segregation**: Maintain strict division between Knowledge (`docs/`), Implementation (`docs/specs/`, code), and Operations (`docs/runbooks/`).
- **Checklist Compliance**: Every new feature ARD must address the mandatory items in the Architecture & Tech Stack Checklist (see root `ARCHITECTURE.md`).

## 4. Engineering Excellence & QA Gates

- **Hard Quality Gates**: Pull Requests strictly require > 80% coverage, zero linting/type errors, and compliance with organizational standards.
- **Traceability**: All PRs must reference the corresponding specification file.

---
_Managed under the [Agentic Pillars](pillar.md)._
