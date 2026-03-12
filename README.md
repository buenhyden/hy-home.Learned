# hy-home-learned

![CI Status](https://github.com/buenhyden/hy-home.Learned/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-0.1.1-orange)
![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)

> An AI-augmented ecosystem designed to bridge the gap between raw learning and production-ready engineering.

## Overview

**hy-home-learned** is a structured, agent-governed workspace built to transform fragmented technical information into reusable knowledge. It solves the "lost-in-translation" problem between learning a new technology and implementing it by providing a unified environment for documentation-driven development.

- **What problem does it solve?** Fragmented knowledge, lack of traceability in AI-assisted coding, and inconsistent documentation standards.
- **Who is it for?** Developers, Data Engineers, and Architects who prioritize high-craft codebases and autonomous AI workflows.
- **Key Features**:
  - **Agentic Core**: Personas, rules, and workflows under `.agent/` for consistent AI behavior.
  - **Knowledge Hub**: A robust `TIL/` system and lazy-loaded documentation protocol.
  - **Spec-Driven Development**: Requirement intent starts in PRDs and flows through ADRs and Specs.
  - **Data Engineering Hub**: Native integration with modern analytical and database toolchains.

## Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.13+ |
| **Frameworks** | FastAPI, Django, Starlette |
| **AI / Agents** | LangChain, LangGraph, Llama-Index |
| **Data Tools** | Polars, Pandas, DBT, DuckDB, Polars |
| **Databases** | PostgreSQL, Neo4j, InfluxDB, Cassandra, Valkey |
| **Orchestration** | Dagster, Luigi, Celery |
| **Environment** | `uv` (Package Management), `ruff`, `mypy` |

## Project Structure

This project follows an AI-Agent-managed, Spec-Driven Development (SDD) structure:

```text
hy-home.Learned/
├── .agent/             # AI Agent rules, workflows, and prompts
├── .claude/            # Shared human-facing agent manuals
├── .github/            # CI/CD workflows and repository templates
├── app/                # Native application source
├── server/             # Backend services and API source
├── web/                # Web frontend application source
├── TIL/                # Atomic knowledge and learning notes
├── docs/               # Project documentation (PRD, ADR, ARD, Guides)
├── operations/         # Operation definitions and infra configs
├── runbooks/           # Operational, incident, and deployment runbooks
├── scripts/            # Utility and automation scripts
├── specs/              # Implementation Plans and API Contracts
├── templates/          # Markdown templates for consistency
├── tests/              # Unit and Integration test suites
├── AGENTS.md           # Master Agent governance
├── GEMINI.md           # Reasoning directives for Gemini
├── CLAUDE.md           # Command directives for Claude Code
└── ARCHITECTURE.md     # High-level system blueprints
```

## Architecture

This ecosystem is governed by three core pillars defined in [ARCHITECTURE.md](./ARCHITECTURE.md):

### 1. Spec-Driven Development (SDD)

Implementation never begins in the source code. It starts in `docs/prd/`, moves to `docs/specs/`, and is only executed once the implementation plan is approved. This eliminates AI hallucinations and ensures architectural integrity.

### 2. AI-Agent Governance

The repository is designed for multi-agent collaboration. Rules in `.agent/rules/` and personas in `AGENTS.md` ensure that every AI interaction follows standardized engineering laws.

### 3. Boundary Segregation

- **Knowledge (`docs/`, `TIL/`)**: The "What" and "Why".
- **Implementation (`specs/`, `app/`, `server/`)**: The "How" and the "Result".
- **Operations (`runbooks/`, `operations/`)**: The "Maintenance" and "Recovery".

## Prerequisites

This repository requires high-performance modern tooling:

- **Python >= 3.13**: Leverages the latest language features and performance fixes.
- **[uv](https://github.com/astral-sh/uv)**: Used for lightning-fast package management and virtual environment handling.
- **Docker** (Optional): Required for containerized deployment and database parity.

## Quick Start

### 1. Clone & Initialize

```bash
git clone https://github.com/buenhyden/hy-home.Learned.git
cd hy-home.Learned
```

### 2. Dependency Management

Use `uv` to create a virtual environment and sync all dependencies:

```bash
uv sync
```

### 3. Environment Configuration

Copy the example environment file and adjust values as needed:

```bash
cp .env.example .env
```

| Variable | Default | Description |
| :--- | :--- | :--- |
| `APP_STAGE` | `dev` | Deployment stage (`dev`, `staging`, `prod`) |

### 4. Git Hooks Setup

Install pre-commit hooks to ensure code quality (Ruff, Mypy, etc.) before every commit:

```bash
uv run pre-commit install
```

### 5. Verified Navigation

Before opening the code, read the master governance files:

- [🤖 **AGENTS.md**](./AGENTS.md): Entrypoint for AI assistants.
- [📚 **docs/README.md**](./docs/README.md): Human-readable knowledge hub.

## Available Scripts

This project uses `uv` for task execution. Below are the primary commands for development and maintenance:

| Command | Description |
| :--- | :--- |
| `uv sync` | Sync dependencies and set up virtual environment. |
| `uv run ruff check .` | Run linter and static analysis. |
| `uv run ruff format .` | Format code to project standards. |
| `uv run mypy .` | Run static type checker. |
| `uv run pytest` | Execute the full test suite. |
| `uv run pre-commit run --all-files` | Run all quality hooks manually. |

## Testing

Quality is enforced through a multi-tier testing strategy. All code must pass automated checks in CI before deployment.

```bash
# Run all tests with coverage reporting
uv run pytest --cov=.

# Run specific test suite
uv run pytest tests/unit/
```

- **Unit Tests**: Colocated with source code or in `tests/`.
- **E2E Tests**: High-level integration tests located in the global `tests/` directory.

## Deployment

Operations are managed via **Runbooks**. This project follows a **Blue-Green Deployment** strategy to ensure zero-downtime releases.

### Environments

- **Development**: Automatic deployment on PR merge to `main`.
- **Staging**: Exact production parity for pre-release validation.
- **Production**: Live environment with strict Infrastructure-as-Code (IaC) governance.

Detailed release procedures and recovery steps are located in:

- [🚀 **OPERATIONS.md**](./OPERATIONS.md): Operational policy and guidelines.
- [📋 **runbooks/**](./runbooks/): Executable operational guides.

## Troubleshooting

- **Dependency Issues**: If `uv sync` fails, ensure you have the latest version of `uv` and Python 3.13 installed. Run `uv self-update`.
- **Environment Errors**: Verify `APP_STAGE` is set in your `.env`. Most application logic branches based on this value.
- **Hook Failures**: If pre-commit hooks fail, use `uv run ruff check . --fix` to auto-resolve common linting issues.
- **Operational Failures**: Consult [runbooks/incident-response-runbook.md](./runbooks/incident-response-runbook.md) for SEV-1/SEV-2 debugging steps.

## Contributing

We welcome contributions that add knowledge or improve the repository. Please read [**CONTRIBUTING.md**](CONTRIBUTING.md), [**AGENTS.md**](AGENTS.md), and [**docs/README.md**](docs/README.md) before starting.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) or repository metadata for details.
