# Tech Stack Standards

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0100-Standards/0150-tech-stack-standard.md`

## 1. Principles

- **Strict Type Integrity**: All source code MUST utilize strict typing. Prohibited use of `any`.
- **Interface-First Architecture**: Public interfaces and data models MUST be defined before implementing logic.
- **Stack-Native Pattern Adherence**: Code MUST align with the project's canonical patterns.

## 2. Requirements

- **Static Analysis Purity**: No code committed that fails mandatory static checks.
- **Narrative Function Decomposition**: Complex logic decomposed into small, intent-revealing functions.
- **Explicit Context Injection**: Dependencies injected via context or providers.

## 3. Must Not

- **Implicit Global Dependencies**: Do NOT rely on undocumented global states.
- **Prototype Pollution**: Avoid modifying native prototypes.

## 4. Validation Criteria

- [ ] build scripts confirm 100% type safety pass.
- [ ] audit confirms explicit, documented interfaces for all modules.
- [ ] Review confirms alignment with established technical stack patterns.
