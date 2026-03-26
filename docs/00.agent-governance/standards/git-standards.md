# Git Standards & Workflows

> **layer:** agentic
> **Status**: Active
> **Source**: Refactored from `.agent/rules/0100-Standards/0110-git-standards.md`

- **Role**: Software Release Engineer
- **Purpose**: Enforce consistent history, atomic changes, and secure version control practices.

## 1. Core Principles

- **[REQ-GIT-01] Conventional Commits**: Messages MUST follow the `type(scope): description` format.
- **[REQ-GIT-02] Atomic Changes**: Every Pull Request (PR) MUST represent exactly one logical change.
- **[REQ-GIT-03] Secret Hygiene**: No secrets, credentials, or `.env` files MUST ever be committed.

## 2. Branching Strategy

| Type | Naming Pattern | Purpose |
| --- | --- | --- |
| Feature | `feat/short-description` | New functionality |
| Fix | `fix/short-description` | Bug repairs |
| Chore | `chore/short-description` | Maintenance / Dependencies |
| Release | `release/X.Y.Z` | Version staging |

## 3. Mandatory Requirements

- **[REQ-GIT-04] Imperative Mood**: Commit descriptions MUST use the imperative mood (e.g., "add", not "added").
- **[REQ-GIT-05] Squash and Merge**: Feature branches MUST be squashed and merged to maintain a clean history.
- **[REQ-GIT-06] PR Documentation**: Every PR MUST include a context description, change list, and testing instructions.

## 4. Prohibited Behaviors

- **[BAN-GIT-01] Vague Commits**: Commits MUST NOT use vague messages like "fix bug" or "WIP".
- **[BAN-GIT-02] Direct Main Commits**: Direct commits to the `main` or protected branches are FORBIDDEN.

## 5. Validation Criteria

- [ ] **[VAL-GIT-01]** Commit header matches standard regex.
- [ ] **[VAL-GIT-02]** No `.env` or sensitive keys are present.
- [ ] **[VAL-GIT-03]** PR contains necessary documentation and visuals for UI.
