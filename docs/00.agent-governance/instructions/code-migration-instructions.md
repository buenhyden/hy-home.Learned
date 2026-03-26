# Code Migration Instructions

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0000-Agents/0014-code-migration-standard.md`

## 1. Principles

- **Safety-First Stability Baseline**: Stability supersedes migration speed.
- **Reversible Incremental Batches**: Decoupled batches with instant revert capability.
- **Dual-Run Verification Discipline**: Parallel verification (Feature Flags) for high-risk tasks.

## 2. Transition Matrix

- **Analysis**: Audit breaking changes in changelogs.
- **Roadmap**: Step-by-step sequential migration plan.
- **Isolation**: Dedicated feature branches or flags.
- **Switch**: Verifiable health-check before final cutover.

## 3. Mandatory Requirements

- **Roadmap Documentation**: Technical roadmap with operations, risks, and rollback.
- **Explicit Compatibility Management**: Ensure backward compatibility for schemas/APIs.
- **Automated Regression Suite Pass**: 100% regression pass on both old and new paths.

## 4. Procedures

- **Pre-migration Impact audit**: Verify transitive dependency tree for conflicts.
- **Post-Migration Cleanup**: Remove deprecated code, flags, and shims.

## 5. Validation Criteria

- [ ] Version-controlled roadmap file exists.
- [ ] 100% test success across source and target implementations.
- [ ] Manual verification of < 10 minute restoration to baseline.
