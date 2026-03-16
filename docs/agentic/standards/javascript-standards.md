# JavaScript Development Standards

> **layer:** agentic
> **Status:** Active
> **Source:** Refactored from `.agent/rules/1600-Javascript/1600-javascript-standard.md`

## 1. Core Principles

- **[REQ-JS-01] ES6+ Primacy**: Use Arrow functions, Destructuring, etc. `var` is BANNED.
- **[REQ-JS-02] Immutable-First**: Favor `const`. Use `map/filter/reduce` over `for` loops.
- **[REQ-JS-03] SRP Functions**: Keep functions small and pure.

## 2. Standards & Tooling

- **Async**: Use `async/await` over callbacks.
- **Errors**: Explicit `try-catch` with structured logging.
- **Formating**: Mandatory `Prettier` and `ESLint` (Airbnb/Standard).
- **JSDoc**: Required for complex functions to define parameter types.

## 3. Architecture

- **Modularity**: Use ES Modules (`import/export`). BANNED: Global namespace pollution.
- **Naming**: Avoid shadowing; follow `camelCase` for vars/funcs.

## 4. Validation

- [ ] ESLint zero-error pass.
- [ ] 100% JSDoc coverage for exposed functions.
- [ ] No legacy patterns (e.g. `XMLHttpRequest`).
