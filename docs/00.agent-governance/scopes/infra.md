# Infrastructure Scope

Use this scope for CI, delivery, infrastructure, and deployment-adjacent repository work.

## Load First

- `.github/workflows/ci.yml`
- `docs/08.operations/README.md`
- `docs/09.runbooks/README.md`

## Task Constraints

- Do not invent infrastructure workflows that are not present in the repository.
- Use CI configuration as the source of truth for validation stages.

## Verification

- Confirm infrastructure references match the active workflow files.
