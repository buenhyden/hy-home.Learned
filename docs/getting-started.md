# Getting Started

Follow these instructions to set up your development environment.

## 🛠 Prerequisites

Ensure you have the following installed:

1. **Python 3.13+**: [Download Python](https://www.python.org/downloads/)
2. **uv**: Fast Python package installer and resolver.

    ```bash
    # Install uv
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

3. **Docker**: For containerized environments. [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

## 🚀 Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/buenhyden/hy-home.Learned.git
    cd hy-home.Learned
    ```

2. **Sync Dependencies**:
    This project uses `uv` to manage dependencies.

    ```bash
    uv sync
    ```

## 📝 IDE Setup

### VS Code (Recommended)

1. Install **VS Code**.
2. Install the **Python** extension.
3. (Optional) Install **Antigravity** or **Cursor** for AI-assisted development.

### Pre-commit Hooks

Set up git hooks to ensure code quality:

```bash
uv tool install pre-commit
pre-commit install
```
