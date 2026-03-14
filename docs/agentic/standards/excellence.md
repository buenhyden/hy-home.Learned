# Engineering Excellence Standards

> **layer:** agentic
> **Status**: Active
> **Source**: Refactored from `.agent/rules/0100-Standards/0140-engineering-excellence-standard.md`

- **Role**: Staff Engineer
- **Purpose**: Define high-level quality bars, automated gates, and technical debt management.

## 1. Quality Gates

- **Test Coverage**: Minimum 80% coverage for new logic.
- **Type Safety**: All Python code MUST pass `mypy --strict`.
- **Naming**: 100% adherence to [Engineering Standards](engineering-standards.md).

## 2. Technical Debt Management

- **[REQ-EXC-01] Debt Identification**: Mark known limitations with `TODO (debt):` comments.
- **[REQ-EXC-02] Cleanup Priority**: Address critical debt that blocks scalability or security immediately.

## 3. Automation Baseline

- EVERY repository MUST use `pre-commit` for basic linting and security checks.
- CI pipelines MUST fail on linting or test regressions.

## 4. Validation Criteria

- [ ] `pre-commit` is active and passing.
- [ ] No regression in test coverage.
- [ ] Zero high-priority security vulnerabilities.
