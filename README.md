# hy-home-learned

![CI Status](https://github.com/buenhyden/hy-home.Learned/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![Version](https://img.shields.io/badge/version-0.1.1-orange)

> A spec-driven, agent-governed project template for Python-centric engineering, documentation, and learning workflows.

## Overview

`hy-home-learned` is a starter repository for teams that want AI-assisted development without undocumented drift. It provides a governed workspace where requirements, architecture, implementation plans, operational runbooks, and contributor tooling are all treated as first-class artifacts.

This repository is designed for:

- New contributors who need a clear local setup and navigation path
- Maintainers who want enforceable documentation and quality gates
- Teams experimenting with AI-assisted workflows while preserving traceability

This repository is not:

- A single ready-to-run SaaS application with one canonical app entrypoint
- A finished infrastructure stack with concrete production deployment config checked in

## Key Features

- Spec-driven development workflow anchored in PRDs, specs, and execution plans
- Agent governance system with personas, rules, workflows, and runtime overlays
- Lazy-loaded documentation hub for ADRs, ARDs, PRDs, specs, plans, runbooks, and operations
- Python-first contributor environment powered by `uv`, Ruff, MyPy, pytest, coverage, and pre-commit
- Reusable template library for README, ADR, PRD, spec, plan, and runbook authoring
- Operational baseline documentation and runbooks for deployment, monitoring, and incident response

## Tech Stack

| Category                         | Technology                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Language                         | Python 3.13+                                                                                                                          |
| Package and runtime tooling      | `uv`                                                                                                                                  |
| Quality tooling                  | Ruff, MyPy, pytest, coverage, pre-commit, Ty                                                                                          |
| Governance and docs              | `.agent/`, `docs/`, `templates/`                                                                                          |
| Representative ecosystem support | FastAPI, Django, Celery, Dagster, dbt, LangChain, LangGraph, LlamaIndex                                                               |
| Databases and data systems       | PostgreSQL, Neo4j, InfluxDB, Cassandra, Valkey, DuckDB                                                                                |
| CI                               | GitHub Actions                                                                                                                        |
| Deployment posture               | Operational baseline only; no concrete Docker, Kubernetes, Vercel, Railway, or Terraform deployment config detected in the repository |

## Prerequisites

Install the following before working in this repository:

- Python 3.13
- [`uv`](https://docs.astral.sh/uv/)
- Git
- Optional: Docker for future service parity or local experiments
- Optional: `pre-commit` if you want the CLI available outside `uv run`

Local setup prepares the workspace, dependencies, and contributor tooling. It does not start a single application process because this repository is a governed template workspace rather than one deployable app.

## Getting Started

This is the highest-value path for a new contributor coming to the repository cold.

### 1. Clone the Repository

```bash
git clone https://github.com/buenhyden/hy-home.Learned.git
cd hy-home.Learned
```

### 2. Verify Python Version

The repository pins Python 3.13 in [`.python-version`](.python-version).

```bash
python --version
```

If your shell is not already using Python 3.13, switch interpreters before syncing dependencies.

### 3. Sync Dependencies

Install the project environment and development dependencies:

```bash
uv sync --dev
```

CI uses a stricter install path with `uv sync --all-extras --dev`, but `uv sync --dev` is the correct default for local contributor setup in the current repository state.

### 4. Configure Environment Variables

Copy the root environment template:

```bash
cp .env.example .env
```

Update values as needed for your local workflow. The root repository currently exposes a minimal shared environment surface; service-specific variables should be documented with the relevant feature spec or service documentation when those components are added.

### 5. Install Git Hooks

Enable the repository quality gates locally:

```bash
uv run pre-commit install
```

This activates the checks defined in [`.pre-commit-config.yaml`](.pre-commit-config.yaml), including formatting, linting, security scanning, type checking, dependency auditing, and test execution at the appropriate commit stages.

### 6. Run Local Quality Checks

Run the same core checks you are expected to pass before opening a PR:

```bash
uv run ruff check .
uv run mypy .
uv run pytest
```

There is no single canonical `uv run dev` command in this repository today. The root project is a governed template workspace, so contributors should start with documentation and quality tooling rather than expecting one application server to launch from the root.

### 7. Use the First 10 Minutes Navigation Path

After setup, read the repository in this order:

1. [`AGENTS.md`](AGENTS.md)
2. [`docs/README.md`](docs/README.md)
3. [`README.md`](README.md)
4. The relevant docs index for your task:
   - [`docs/prd/README.md`](docs/prd/README.md)
   - [`docs/specs/README.md`](docs/specs/README.md)
   - [`docs/plans/README.md`](docs/plans/README.md)
   - [`docs/runbooks/README.md`](docs/runbooks/README.md)

## Environment Variables

The root repository currently documents one shared environment variable.

| Variable    | Required | Default | Allowed Values           | Description                                                             |
| ----------- | -------- | ------- | ------------------------ | ----------------------------------------------------------------------- |
| `APP_STAGE` | Yes      | `dev`   | `dev`, `staging`, `prod` | Selects the active repository execution profile and environment context |

Feature-specific or service-specific variables should be documented alongside the relevant spec, service module, or operational guide instead of being guessed into the root README.

## Repository Structure

The README template has been adapted to the directories that actually exist in this repository.

```text
hy-home.Learned/
├── .agent/             # Agent rules, workflows, and repository-specific governance
├── .claude/            # Shared runtime manuals behind root AI entrypoints
├── .github/            # CI workflows and repository automation
├── TIL/                # Knowledge notes and learning artifacts
├── docs/               # PRDs, ADRs, ARDs, specs, plans, runbooks, and operations indexes
├── examples/           # Example documents showing template usage
├── scripts/            # Utility and automation scripts
├── templates/          # Canonical Markdown templates for project artifacts
├── tests/              # Global integration, E2E, and repository-level test guidance
├── AGENTS.md           # Vendor-neutral AI agent entrypoint
├── CLAUDE.md           # Claude runtime entrypoint
├── GEMINI.md           # Gemini runtime entrypoint
├── ARCHITECTURE.md     # High-level architecture law and constraints
├── OPERATIONS.md       # Operational policy baseline
├── CONTRIBUTING.md     # Contribution rules and PR expectations
├── COLLABORATING.md    # Human/AI collaboration workflow
├── pyproject.toml      # Python project metadata and tool configuration
├── .pre-commit-config.yaml
├── .env.example
└── README.md
```

## How the System Works

### Documentation Chain

The repository is designed to move work through explicit documents instead of jumping straight into code:

1. **PRD** defines the problem, scope, and success criteria.
2. **ADR / ARD** records architectural decisions and structural boundaries.
3. **Spec** defines the implementation contract.
4. **Plan** breaks approved work into executable steps.
5. **Implementation and Runbooks** carry the result into code and operations.

The docs hub at [`docs/README.md`](docs/README.md) is the entrypoint for this chain.

### Governance Chain

The repository’s governance path is intentionally layered:

1. [`AGENTS.md`](AGENTS.md) defines the vendor-neutral agent entrypoint.
2. [`docs/agentic/shared-governance.md`](docs/agentic/shared-governance.md) defines shared rules for all active runtimes.
3. Runtime entrypoints such as [`CLAUDE.md`](CLAUDE.md) and [`GEMINI.md`](GEMINI.md) add model-specific overlays.
4. [`.agent/rules/`](.agent/rules) and [`.agent/workflows/`](.agent/workflows) provide enforceable standards and execution guidance.

### Quality Gates

Contributor quality is enforced in three places:

- **Local hooks** via [`.pre-commit-config.yaml`](.pre-commit-config.yaml)
- **Tool configuration** via [`pyproject.toml`](pyproject.toml)
- **CI verification** via [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

The current CI workflow installs Python 3.13, syncs dependencies with `uv`, then runs pre-commit checks at both the `commit` and `pre-push` stages across the repository.

### Operational Model

Operational policy and procedure are intentionally separated:

- [`OPERATIONS.md`](OPERATIONS.md) defines environment hierarchy, deployment policy, observability expectations, and continuity requirements.
- [`docs/runbooks/`](docs/runbooks) contains the executable runbooks for deployment, monitoring, and incident response.

## Available Commands

Use the following validated commands from the repository root.

| Command                                                   | Purpose                                                       |
| --------------------------------------------------------- | ------------------------------------------------------------- |
| `uv sync`                                                 | Install the base project environment                          |
| `uv sync --dev`                                           | Install the project environment plus development dependencies |
| `uv run pre-commit install`                               | Install repository git hooks locally                          |
| `uv run pre-commit run --all-files --hook-stage commit`   | Run the fast commit-stage checks across the repository        |
| `uv run pre-commit run --all-files --hook-stage pre-push` | Run the heavier pre-push checks across the repository         |
| `uv run ruff check .`                                     | Run Ruff linting                                              |
| `uv run ruff format .`                                    | Format supported files with Ruff                              |
| `uv run mypy .`                                           | Run static type checking                                      |
| `uv run pytest`                                           | Run the configured pytest suite                               |
| `uv run pytest --cov=.`                                   | Run tests with coverage output                                |

## Testing and Quality

The root pytest configuration lives in [`pyproject.toml`](pyproject.toml).

### Pytest Defaults

The configured defaults currently include:

- Parallel execution with `-n auto`
- Coverage collection with terminal missing-line reporting
- HTML report generation to `report.html`
- Test discovery across `libs/*/tests`, `services/*/tests`, and `tests`
- Automatic async test support

Because the repository is template-oriented, some configured search paths may only become active once future services or libraries are added.

### Coverage and Contribution Expectations

[`CONTRIBUTING.md`](CONTRIBUTING.md) sets the expectation that contributions should meet or maintain a coverage baseline above 80%, pass linting and type checks, and comply with the repository’s governing standards.

### Test Placement Model

[`tests/README.md`](tests/README.md) distinguishes between:

- **Co-located unit tests** for component-local behavior
- **Global `tests/` suites** for integration, E2E, and repository-level coverage

When adding new code, use the repository testing guidance rather than assuming all tests belong under the root `tests/` directory.

## Deployment and Operations

This section describes the repository’s **operational baseline**, not a concrete production deployment recipe.

### What Exists Today

- Environment hierarchy is defined as **development**, **staging**, and **production**
- Deployment policy favors **blue-green deployment** or progressive delivery for eligible services
- CI gates must pass before release activity
- Observability expectations cover metrics, structured logging, tracing, alerts, backups, RTO, and RPO
- Runbooks exist for deployment, monitoring, and incident response

### What Does Not Exist Yet

No concrete Docker, Kubernetes, Vercel, Railway, or Terraform deployment configuration is currently checked into the repository root.

### Operational References

- [`OPERATIONS.md`](OPERATIONS.md)
- [`docs/runbooks/deployment-runbook.md`](docs/runbooks/deployment-runbook.md)
- [`docs/runbooks/incident-response-runbook.md`](docs/runbooks/incident-response-runbook.md)
- [`docs/runbooks/monitoring-runbook.md`](docs/runbooks/monitoring-runbook.md)

Use these documents as the policy and procedure baseline when real deployable services are added to the repository.

## Troubleshooting

### Python Version Mismatch

If dependency sync or tooling fails immediately, confirm that your shell is using Python 3.13:

```bash
python --version
cat .python-version
```

### `uv` Missing or Outdated

If `uv` is not available, install or upgrade it before continuing:

```bash
uv --version
```

### `uv sync --dev` Fails

Common causes are:

- Wrong Python interpreter
- Corrupted local virtual environment
- Transient dependency resolution issues

Start by retrying after confirming Python 3.13. If the local environment is inconsistent, remove and recreate the virtual environment using your normal `uv` workflow.

### Pre-commit Hook Failures

Hook failures usually indicate real repository issues rather than bad hook configuration. Re-run the failing stage directly:

```bash
uv run pre-commit run --all-files --hook-stage commit
uv run pre-commit run --all-files --hook-stage pre-push
```

### Ruff, MyPy, or pytest Failures

Run the failing tool in isolation first:

```bash
uv run ruff check .
uv run mypy .
uv run pytest
```

Fix one class of failure at a time rather than trying to resolve all output at once.

### Not Sure Where to Start in the Docs

Start from [`docs/README.md`](docs/README.md), then open only the relevant index for your task. Do not jump directly into random deep files without using the docs hub first.

### Looking for a Single App Startup Command

There is no single root application startup command because the repository is a template workspace. Start with governance, docs, and quality tooling first; add service-specific startup instructions only in the relevant module or service docs as those components are introduced.

## Contributing

Use [`CONTRIBUTING.md`](CONTRIBUTING.md) as the detailed source of truth. The short version is:

1. Start with the correct document or template when your contribution changes requirements, architecture, or operations.
2. For code-bearing feature work, anchor the change in the relevant spec and plan before implementation.
3. Use branch names such as `feature/...`, `fix/...`, or `docs/...`.
4. Use Conventional Commits.
5. Run local QA gates before opening a PR.
6. Reference the relevant spec in your PR when code is added.

Useful references:

- [`COLLABORATING.md`](COLLABORATING.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- [`AGENTS.md`](AGENTS.md)

## License

No standalone `LICENSE` file is currently present in the repository. If this template is intended for public reuse, add a license file and update this section accordingly.
