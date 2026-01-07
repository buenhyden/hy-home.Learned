# Python Data Engineering & Data Science General Rules

## Scope and Goals

- The agent must write Python code, project structures, and configurations that are independent of any hard-coded file system paths.
- All data workflows must be reproducible, version-controlled, and understandable to collaborators.
- The agent should promote practices suitable for both data engineering (pipelines, ETL/ELT) and data science (analysis, modeling, experiments).

## Path-agnostic Code and Data Handling

- Never use absolute paths such as `/Users/username/project` or `C:\data\project` in code or notebooks.
- Use project-root–relative paths and configurable base directories instead, for example:
  - `BASE_DIR = Path(__file__).resolve().parents[1]`
  - Data paths like `BASE_DIR / "data" / "raw"` or `"data/raw"` relative to the repository root.
- When a project structure is absent or unclear, the agent must:
  - Propose a standard, path-agnostic layout with `data/`, `src/`, `notebooks/`, and `config/` directories.
  - Ask the user to confirm or adjust the proposed structure.

## Project Structure and Modularity

- Prefer a standard, modular project layout for Python data projects, for example:
  - `data/raw`, `data/processed`, `data/interim` for different data states.
  - `src/` for reusable Python modules (ingestion, preprocessing, features, models).
  - `notebooks/` for exploration only; production logic must live in `src/`.
- Keep transformation logic in functions and modules, not in ad hoc scripts or notebook cells.
- Avoid duplicating logic across scripts; follow DRY (Don’t Repeat Yourself) principles.

## Reproducible Environments

- Always rely on explicit environment specifications such as:
  - `pyproject.toml`, `requirements.txt`, `environment.yml`, or equivalent.
- The agent must:
  - Avoid installing packages “by hand” in ways that are not captured in environment files.
  - Prefer pinned or constrained versions for critical libraries (for example, pandas, numpy, scikit-learn, PySpark) to ensure reproducibility.
- Environment setup instructions must not depend on specific host paths; use generic commands (`python -m venv`, `conda env create`, `pip install -r requirements.txt`) that work from the project root.

## Data Engineering Pipeline Principles

- Prefer orchestrated, scheduled pipelines (for example, Airflow, Dagster, Prefect, dbt, or similar tools) over ad hoc cron jobs or manual script chains.
- Pipelines must be:
  - Idempotent (safe to run multiple times).
  - Observable (logging, metrics, basic monitoring).
  - Version-controlled (pipeline definitions and code checked into the repository).
- Choose ETL vs ELT based on use case and clearly document the chosen approach.

## Data Science Workflow Principles

- Separate concerns:
  - Use notebooks for exploration, visualization, and communication.
  - Use `src/` for reusable code (data loading, feature engineering, model training, evaluation).
- Ensure that any notebook-based analysis can be executed via a script or pipeline entry point (for example, `python src/train.py`) without manual UI steps.
- Record configurations (hyperparameters, dataset versions, feature sets) in configuration files (YAML/TOML/JSON) rather than hard-coding them in notebooks.

## Data Access and APIs

- When extracting data via Python HTTP clients or APIs:
  - Use robust patterns for pagination, retries, timeouts, and backoff.
  - Avoid embedding credentials in code; use environment variables or secret managers.
- Avoid hard-coding host-specific endpoints or file shares; use configuration and environment variables instead.

## Quality, Testing, and Validation

- Encourage unit, integration, and data-quality tests using tools such as `pytest`, `great_expectations`, or library-specific validators.
- Validate input and output schemas for pipeline steps, ensuring that upstream changes do not silently break downstream tasks.
- Include tests and validation that do not rely on absolute paths or local-only resources; use test fixtures and relative paths under `tests/` and `data/`.

## Documentation and Collaboration

- Every project must include a `README` describing:
  - Purpose of the project.
  - Directory structure and conventions.
  - How to set up the environment and run key pipelines or experiments.
- The agent should promote version control (for example, Git) and discourage using notebooks as the only source of truth for production logic.
- Important decisions (for example, choice of ETL vs ELT, schema changes, major modeling approaches) should be documented in code comments or markdown files under `docs/` or similar.
