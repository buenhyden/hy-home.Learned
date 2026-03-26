# Debugging Agent Instructions

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0000-Agents/0015-debugging-standard.md`

## 1. Principles

- **Systematic Root Cause Isolation**: Use binary search or logical deduction.
- **Hypothesis-Driven Investigation**: Generate ranked causes first.
- **Mandatory minimal Reproduction**: Create a test that demonstrates the defect.

## 2. Requirements

- **Verified Regression Prevention**: Fix must include a passing regression test.
- **Explicit State Inspection**: Use strategic logging or debuggers.
- **Documentation of Residual Risks**: Document introduced side-effects.

## 3. Procedures (The RCA Loop)

- IF a fix fails THEN discard hypothesis and generate a new investigative path.
- UPON resolution THEN remove all temporary debugging logs.

## 4. Validation Criteria

- [ ] Failing test case established before fix.
- [ ] Patch addresses only root cause.
- [ ] All tests pass after fix.
