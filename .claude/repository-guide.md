# Repository Operating Guide

This manual contains repository-specific operating detail reused across agent
runtimes.

## Toolchain

- Python 3.13+
- Package manager and task runner: `uv`
- Primary Python source today: `TIL/`
- Future service areas: `libs/`, `services/`

## Common Commands

```bash
uv sync --dev
uv run ruff check .
uv run ruff format .
uv run ty check
uv run mypy --strict .
uv run pytest
uv run pytest tests/path/to/test_file.py::test_name
uv run pytest --cov=. --cov-report=term-missing
uv run pre-commit install
uv run pre-commit run --all-files --hook-stage commit
uv run pre-commit run --all-files --hook-stage pre-push
uv run cz commit
```

## Quality Gates

- Total test coverage must stay at or above 80%.
- Docstring coverage for `TIL/` must stay at or above 80%.
- Absolute imports only; relative imports are banned repo-wide.
- Maximum line length: 120.
- Docstrings use the Google convention.
- Maximum cyclomatic complexity: 10.
- `ty` is the fast commit-stage type check; `mypy --strict` is the slower
  push-stage type gate.
- Tests may use `assert`; production code may not.

## Documentation Contract

- Human-readable repository knowledge lives in [docs/](../docs/README.md).
- Approved implementation context lives in `docs/prd/`, `docs/adr/`,
  `docs/specs/`, and `docs/plans/`.
- Operational procedures live in `docs/runbooks/`; incident and postmortem
  records live in `docs/operations/`.
- Use [templates/](../templates/) when creating governed repository documents.

## Automation Gates

| Stage        | Checks                                                                                                           |
| :----------- | :--------------------------------------------------------------------------------------------------------------- |
| `pre-commit` | ruff, ty, detect-secrets, gitleaks, bandit, markdownlint, prettier, shellcheck, complexipy, hadolint, actionlint |
| `pre-push`   | mypy --strict, pip-audit, pytest                                                                                 |
| `commit-msg` | commitizen                                                                                                       |

---

_Last Updated: March 2026_
