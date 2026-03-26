# Code Test Writing Instructions

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0000-Agents/0017-code-test-writing-standard.md`

## 1. Principles

- **Mandatory AAA Structure**: Arrange-Act-Assert pattern for all tests.
- **Isolation-First Unit Testing**: No external dependencies; use mocks.
- **Meaningful Behavior Verification**: Verify outcomes, not implementation details.

## 2. Test Matrix

- **Unit**: Atomic isolation & 100% logic coverage.
- **Integration**: Component interaction & side-effect verification.
- **E2E**: Happy-path flows in realistic environments.
- **Mocks**: Deterministic responses & call verification.

## 3. Mandatory Requirements

- **Coverage of Happy and Sad Paths**: 100% Happy Path, 80% Edge Cases/Errors.
- **Explicit Test Traceability**: Link tests to REQ or feature.
- **Independent Test Readiness**: Self-contained tests with state reset.

## 4. Procedures

1. **Analyze inputs/outputs**
2. **Scaffold AAA blocks**
3. **Mock dependencies**
4. **Implement assertions**
5. **Verify local pass**

## 5. Validation Criteria

- [ ] 100% of new tests use explicit AAA comments.
- [ ] All new logic branches exercised.
- [ ] Suite passes consistently across 10 repeated runs.
