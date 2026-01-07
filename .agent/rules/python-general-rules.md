# Python General Rules

## Style and Readability

- Follow PEP 8 for code style (indentation with 4 spaces, naming, imports, line length, etc.) unless the repository has a clearly documented alternative style guide. [web:168][web:172]
- Prefer clear, explicit code over clever but obscure constructs; optimize first for readability and maintainability. [web:174][web:173]
- Use meaningful names:
  - snake_case for functions, variables, and modules.
  - PascalCase for classes.
  - UPPER_SNAKE_CASE for constants. [web:168][web:182]
- Add docstrings to public modules, classes, and functions to explain intent, parameters, and return values. [web:174][web:187]
- Keep functions and methods short and focused on a single responsibility where possible. [web:174][web:180]

## Project Structure and Paths

- Do not hard‑code absolute file system paths (for example, `/home/user/project`, `C:\Users\name\project`) in code. [web:175][web:184]
- Use project‑relative paths and `pathlib.Path` (or equivalent) and, when needed, configuration files or environment variables to specify locations. [web:175][web:181]
- Prefer a structured layout with clearly separated concerns (for example, `src/` for code, `tests/` for tests, `configs/` for configuration, `docs/` for documentation) and follow existing conventions in the repository. 
- Avoid putting executable logic at import time in `__init__.py`; keep package initializers minimal, used mainly for exports. 

## Environment and Dependencies

- Never rely on globally installed packages; assume a project‑specific virtual environment or tool (for example, venv, conda, Poetry, uv). 
- Record dependencies in a standard file (`pyproject.toml`, `requirements.txt`, or `environment.yml`) instead of instructing ad hoc pip installs in comments or docs only. 
- Prefer pinned or constrained versions for critical dependencies when reproducibility is important. 
- Do not hard‑code secrets, credentials, or API keys in Python code; use environment variables or dedicated secret management instead. 

## Error Handling and Logging

- Use exceptions and explicit error handling rather than silent failures or broad `except:` clauses. 
- Catch only specific exceptions where possible and log meaningful context when errors occur.
- Use the standard `logging` module (or the project’s logging setup) instead of `print` for operational logs. 
- Avoid exposing sensitive data (for example, passwords, tokens) in logs or error messages. 

## Testing and Code Quality

- Encourage automated tests, preferably using `pytest`, with a test structure that mirrors the main package (for example, `tests/` mirroring `src/` or package layout). 
- When adding or modifying code, add or update tests to cover typical cases and key edge cases.
- Use linters and formatters (for example, Ruff/Flake8, Black, isort, mypy or pyright for type checking) if the project already uses them, and respect existing configuration. 
- Aim for clear boundaries between pure logic (easier to test) and I/O or side‑effects (wrapped at the edges). 

## Reproducibility and Collaboration

- Assume code will be run on different machines and environments; avoid machine‑specific assumptions (paths, shell, OS) in Python modules. 
- Document important usage patterns, assumptions, and required environment variables in `README` or appropriate docs, not only in comments. 
- Prefer deterministic behavior when possible (for example, seeding random number generators when reproducibility is required), and document any non‑deterministic aspects. 

## Performance and Resource Usage

- Optimize only after establishing correctness and clarity; when optimizing, measure and document the reasons and results. 
- Use appropriate data structures and libraries (for example, list vs deque, sets for membership checks, vectorized operations in numerical code) instead of premature micro‑optimizations. 
- Avoid unnecessary loading of large data into memory; prefer streaming or chunked processing when dealing with big files or datasets. 
