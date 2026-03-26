# Engineering Excellence Standards

> **layer:** agentic
> **Status:** Active
> **Source:** Refactored from `.agent/rules/0100-Standards/0140-engineering-excellence.md`

## 1. Core Principles

- **[REQ-ENG-01] Intent-Revealing Declarativity**: Code MUST explain "why" through naming and structure.
- **[REQ-ENG-02] Single Responsibility (SRP)**: Every function/class MUST have one reason to change.
- **[REQ-ENG-03] Defensive Failure**: Logic MUST "Fail Fast" using guard clauses.

## 2. Mandatory Standards

- **[REQ-ENG-08] Type Annotations**: Mandatory for all public signatures.
- **[REQ-ENG-09] Narrative Structure**: High-level orchestrators top, implementation helpers bottom.
- **[BAN-ENG-01] No Magic Variables**: Use named constants/enums.
- **[BAN-ENG-02] No Indentation Hell**: No nesting > 3 levels.

## 3. Systematic Debugging (RCA)

- IF recurring bug THEN MUST perform Root Cause Analysis (5 Whys).
- Allocate 10% of cycle for proactive refactoring.

## 4. Validation

- [ ] Lint/Format pass.
- [ ] coverage > 80%.
- [ ] SRP compliance verification.
