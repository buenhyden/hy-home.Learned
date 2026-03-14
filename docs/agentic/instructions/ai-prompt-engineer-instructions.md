# AI Prompt Engineer Instructions

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0000-Agents/0001-ai-prompt-engineer-agent.md`

## 1. Principles

- **Structural Integrity (Role-Context-Task)**: Persona -> Context -> Task -> Output Format.
- **Persona-First Grounding**: Define expert persona to steer tone and reasoning.
- **Explicit Constraint Enumeration**: List non-negotiable functional/stylistic items.

## 2. Design Matrix

- **Planning**: Methodical strategy selection (CoT, Few-Shot).
- **Layout**: Clear separation of instructions and data.
- **Validation**: Anti-injection guardrails.
- **Format**: Explicit output structure (JSON/Markdown).

## 3. Mandatory Requirements

- **Verifiable Context Isolation**: Use separators like `[CONTEXT]` or `---`.
- **Explicit Reasoning Chains**: Instruct model to "think step-by-step".
- **Zero-Ambiguity Directives**: Use deterministic verbs (Generate, Extract, Verify).

## 4. Procedures

- **Prompt Audit Flow**: Perform "Red Teaming" for system prompt modifications.
- **Iterative Refinement**: Analyze failures and adjust constraint clarity.

## 5. Validation Criteria

- [ ] Clear persona defined in first 10% of prompt.
- [ ] Output strictly obeys 100% of defined constraints.
- [ ] Dynamic data visually separated from directives.
