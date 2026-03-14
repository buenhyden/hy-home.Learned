# Refactoring Agent Instructions

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0000-Agents/0013-refactoring-standard.md`

## 1. Principles

- **Mandatory behavior Preservation**: Refactoring MUST NOT change runtime behavior.
- **Green-to-Green Test Cycle**: Start and end with passing tests.
- **Atomic Incrementalism**: Small, verifiable steps only.

## 2. Requirements

- **Prioritized Smell Resolution**: Target specific smells (God Object, Duplicated Code).
- **Explicit Diff Rationale**: Document "Why" the new structure is superior.
- **Synchronized Documentation**: Update JSDoc/README immediately.

## 3. Procedures (The Refactor Loop)

1. Verify Baseline (Green)
2. Identify Smell
3. Apply Atomic Pattern
4. Verify Result (Green)
5. Document Change

## 4. Validation Criteria

- [ ] 100% of tests pass before/after.
- [ ] Reduction in Cyclomatic Complexity confirmed.
- [ ] JSDoc/types accurately reflect structural changes.
