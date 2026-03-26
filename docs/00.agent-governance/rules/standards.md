# Shared Governance Standards

These standards apply to every task that uses the active governance system.

## Non-Negotiables

- Use the numeric docs taxonomy as the only active documentation map.
- Do not silently skip persona or scope selection.
- Keep instructions concise and modular.
- Avoid stale paths, deleted directories, and URI-style file links in active governance docs.
- Verify touched files before completion.

## Traceability

- Requirements live in `docs/01.prd/`.
- Technical contracts live in `docs/04.specs/`.
- Execution history lives in `docs/05.plans/`.
- Update impacted README files when structure or responsibilities change.

## Execution Posture

- Read first, mutate second.
- Prefer the narrowest relevant scope file.
- Do not load broad governance fragments when a task-specific scope exists.
- Keep provider details inside `providers/`, not in root files.
