# Agentic Reasoning Standards

> **Layer**: agentic
> **Status**: Active Detail layer

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

## 2. Advanced Error Handling

- **Tool Output Fidelity**: Report full output (STDOUT/STDERR) to enable subsequent reasoning transitions.
- **Failure Analysis**: If a primary tool fails, reason about whether it's a project issue or a system failure before retrying.

---
_Managed under the [Agentic Pillars](pillar.md)._
