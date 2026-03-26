# Pre-Task Checklist

This checklist is mandatory for governance-driven work.

## Phase 1: Pre-Task Gate

- [ ] Confirm goal, scope, and success criteria.
- [ ] Identify the active persona via `persona.md`.
- [ ] Identify one active scope file in `scopes/`.
- [ ] Confirm traceability anchors:
  - [ ] Requirement anchor in `docs/01.prd/` or contract anchor in `docs/04.specs/`
  - [ ] Execution tracking anchor in `docs/05.plans/`
- [ ] Confirm language policy for touched files.
- [ ] Load only the minimum required governance files.

## Phase 2: During-Task Gate

- [ ] Re-check whether changed structure requires README synchronization.
- [ ] Re-check path references when adding or moving links.
- [ ] Keep provider-specific details in `providers/`, not in root files.
- [ ] Keep root entrypoint files thin.
- [ ] Preserve `.agent/` as compatibility-only unless explicitly requested.

## Phase 3: Pre-Completion Gate

- [ ] Run stale-path and broken-link checks from `path-validation.md`.
- [ ] Verify no Korean text exists in `docs/00.agent-governance/`.
- [ ] Verify `CLAUDE.md` and `GEMINI.md` import chains are valid.
- [ ] Verify root line-budget guidance in `quality-standards.md`.
- [ ] Verify updated docs reflect final completed structure.
