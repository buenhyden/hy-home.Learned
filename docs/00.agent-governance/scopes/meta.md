# Meta Governance Scope

Use this scope for agent bootstrap files, routing rules, provider notes, and governance refactor tasks.

## Load First

- `AGENTS.md`
- `../rules/bootstrap.md`
- `../rules/pre-task-checklist.md`
- `../rules/persona.md`
- `../rules/documentation-protocol.md`
- `../rules/docs-lifecycle-matrix.md`

## Task Constraints

- Keep root entrypoint files thin and predictable.
- Keep governance structure aligned with `rules/`, `scopes/`, `providers/`, and `memory/`.
- Preserve `.agent/` as compatibility-only unless explicitly requested.
- Do not edit existing authored content under `docs/01~99/` in this scope.

## Verification

- Run `../rules/path-validation.md` checks.
- Validate structure, language policy, provider import chain, and README synchronization.
