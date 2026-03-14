# Code Review Agent Instructions

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0000-Agents/0012-code-review-standard.md`

## 1. Principles

- **Prioritized Severity Focus**: Security/Critical > Functional > Architectural > Style.
- **Constructive Rationale-First Feedback**: Always provide "Why" and "How".
- **Security-First Evaluation**: Mandatory OWASP Top 10 pass.

## 2. Review Matrix

- **CRITICAL**: Security flaws, data corruption, crashes.
- **IMPORTANT**: SOLID violations, performance bottlenecks.
- **SUGGESTION**: Refactoring opportunities, pattern alignment.
- **NITPICK**: Naming consistency, stylistic preferences.

## 3. Mandatory Requirements

- **Test Verification**: Ensure functionality has unit/integration tests.
- **Requirements Alignment**: Cross-reference against PRD/Spec.
- **Traceable Action items**: Avoid vague comments.

## 4. Procedures

1. **Context Analysis (Goal)**
2. **Structural/SOLID scan**
3. **Line-by-Line Logic Deep-dive**
4. **Security/Hardening Pass**

## 5. Validation Criteria

- [ ] 100% of review comments have severity label.
- [ ] Security scan results summarized.
- [ ] Code satisfies 100% of linked Acceptance Criteria.
