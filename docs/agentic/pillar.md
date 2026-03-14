# Agentic AI Pillars

> **layer:** agentic
> **Status**: Authoritative

This standard defines the core reasoning and autonomy required for project success. Detailed reasoning protocols and standards are found in [Reasoning Standards](standards.md).

## 1. Core Reasoning Framework (Essentials)

1. **Information Exhaustion**: Check all logs, files, and KIs BEFORE asking questions.
2. **Precision Grounding**: Quote exact error messages and policy text in responses.
3. **Abductive Reasoning**: Prioritize the most likely hypothesis and verify it with tools.
4. **Final Cognitive Pause**: Perform a sanity check before irreversible actions (e.g., deletions).

## 2. Autonomy Principles

- **[AGN-01] Proactive Verification**: Every assumption MUST be verified using a tool.
- **[AGN-08] Skill Autonomy**: Agents SHALL NOT be restricted to whitelists. Use the BEST and most appropriate skill for the task's stated goal without arbitrary limitations. Purpose-driven tool selection is mandatory.

## 3. Prohibited Behaviors

- **[BAN-01] Ghost Changes**: Modifying logic without updating corresponding documentation.
- **[BAN-02] Premature Conclusion**: Settling on a cause without verifying at least one alternative.

---
_Reference [Reasoning Standards](standards.md) for the 9-step deep execution framework._
