# 💻 Tech Stack Details

This workspace uses a curated modern stack designed for reliability, speed, and strictness.

## 🏗️ Core Infrastructure

| Component | Technology | Reasoning |
| --- | --- | --- |
| **Language** | **Python 3.13+** | Performance improvements (JIT) and latest typing features. |
| **Manager** | **[uv](https://github.com/astral-sh/uv)** | Replaces pip/poetry. extremely fast, unified toolchain. |
| **VCS** | **Git** | Standard version control. |

## 🛡️ Governance & Quality

| Tool | Purpose | Config File |
| --- | --- | --- |
| **[Ruff](https://github.com/astral-sh/ruff)** | Linting & Formatting | `pyproject.toml` |
| **[Mypy](https://github.com/python/mypy)** | Static Type Checking | `pyproject.toml` |
| **[Pre-commit](https://pre-commit.com)** | Git Hooks | `.pre-commit-config.yaml` |
| **[Yamllint](https://github.com/adrienverge/yamllint)** | YAML Linting | `.pre-commit-config.yaml` |

## 🧪 Research & Data Science (Potential)

*As listed in `pyproject.toml` dependencies:*

- **Data Processing**: `pandas`, `polars`, `duckdb`
- **Machine Learning**: `scikit-learn`, `xgboost`
- **AI/LLM**: `langchain`, `llama-index`, `transformers`
- **Visualization**: `matplotlib`, `seaborn`

## 🤖 Automation

- **Task Runner**: `uv run`
- **CI/CD**: GitHub Actions (Workflows in `.github/workflows`)
