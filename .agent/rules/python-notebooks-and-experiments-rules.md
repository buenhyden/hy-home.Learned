# Python Notebooks and Experiments Rules

## Role of Notebooks

- Use notebooks for:
  - Data exploration and visualization.
  - Early-stage experiments and reporting.
- Do not run production data pipelines directly from notebooks; production logic should live in `src/` and be callable from the command line or orchestrators.

## Reproducibility of Notebooks

- Notebooks must:
  - Be runnable top-to-bottom without manual edits or path adjustments.
  - Use relative imports and relative paths, relying on the project structure.
- Ensure that each notebook explicitly records:
  - Environment information (for example, Python version, key library versions).
  - Dataset versions or snapshot identifiers.

## Transition from Notebooks to Modules

- When notebook experiments stabilize:
  - Extract reusable functions and classes into `src/` modules.
  - Keep notebooks minimal and focused on examples and visualizations that call into `src/`.
- Avoid long, monolithic notebooks with critical logic duplicated in multiple places.

## Experiment Tracking

- Encourage use of experiment-tracking tools (for example, MLflow, Weights & Biases, or simple CSV/JSON logs) to:
  - Record hyperparameters, metrics, and artifacts for each run.
  - Support comparison and rollback of models and configurations.
- Store experiment outputs in project-relative directories such as `models/`, `reports/`, or `artifacts/`, not in user-specific paths.
