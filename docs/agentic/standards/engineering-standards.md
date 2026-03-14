# Engineering Standards

> **layer:** agentic
> **Status**: Active
> **Source**: Refactored from `.agent/rules/0100-Standards/0104-engineering-standard.md`

- **Role**: Staff Engineer
- **Purpose**: Enforce universal standards for code quality, strict maintainability, and systematic debugging.

## 1. Core Principles

- **[REQ-ENG-CLN-01] Intent-Revealing**: Names MUST describe *what* a variable holds or *what* a function does.
- **[REQ-ENG-CLN-02] Single Responsibility**: Functions and classes MUST have one reason to change.
- **[REQ-ENG-CLN-03] DRY**: Logic MUST NOT be duplicated. Abstract repeated patterns.
- **[REQ-ENG-CLN-04] KISS**: Simple code MUST be preferred over clever code.
- **[REQ-ENG-CLN-05] YAGNI**: Implement ONLY what is needed today.

## 2. Standards & Constraints

### 2.1 Casing and Naming

- **TS/JS/Go**: `camelCase` for vars/funcs, `PascalCase` for classes.
- **Python/Rust**: `snake_case` for vars/funcs.
- **Constants**: `SCREAMING_SNAKE_CASE`.
- **Booleans**: MUST use prefixes: `is`, `has`, `should`, `can`.

### 2.2 Style Restrictions

- **[BAN-ENG-STY-01] No Magic Numbers**: Replace numeric literals with named constants.
- **[BAN-ENG-STY-02] No Nested Else**: Use Guard Clauses (early returns) to flatten nesting.

## 3. Mandatory Procedures

### 3.1 Object Calisthenics (Strict)

1. **One Level of Indentation**: Extract methods to flatten logic.
2. **Tell, Don't Ask**: Encapsulate logic with data; don't just expose getters.
3. **Wrap Primitives**: Use Value Objects (e.g., `Email`) instead of raw strings where validatable.

### 3.2 Systematic Debugging

1. **Context**: Read valid logs and error messages.
2. **Reproduce**: Create a minimal reproduction case.
3. **Hypothesis**: Formulate a "Because of X, Y happens" theory.
4. **Fix**: Apply minimal fix + Regression Test.

## 4. Examples

### Clean Code (Guard Clauses)

```typescript
// GOOD: Guard Clauses
function processUser(user) {
  if (!user) return;
  if (!user.isActive) return;
  if (!user.hasCredit) return;

  charge(user);
}
```

## 5. Validation Criteria

- [ ] **[VAL-ENG-NAM-01]** Naming follows language conventions.
- [ ] **[VAL-ENG-STY-01]** No deep nesting (>3 levels).
- [ ] **[VAL-ENG-STY-02]** No magic numbers/strings without constants.
- [ ] **[VAL-ENG-TST-01]** Fixes include regression tests.
