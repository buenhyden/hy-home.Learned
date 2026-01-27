# 🛠️ Development Setup Guide

This guide ensures a consistent development environment for both human developers and AI agents.

## 📋 Prerequisites

- **OS**: Windows (preferred), macOS, or Linux.
- **Python**: Version **3.13+** required.
- **Package Manager**: [`uv`](https://github.com/astral-sh/uv) (Extremely fast Python package installer).
- **Git**: Latest version.

## ⚡ Quick Start

### 1. Install `uv`

If you haven't installed `uv` yet:

```powershell
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone and Sync

Clone the repository and sync dependencies. `uv` handles the virtual environment creation automatically (`.venv`).

```bash
git clone <repository-url>
cd hy-home-learned
uv sync
```

### 3. Install Git Hooks

We use `pre-commit` to ensure code quality (linting, formatting, typo checks) before every commit.

```bash
# Activate the virtual environment if needed (uv usually handles this, but for manual activation)
# .venv\Scripts\activate

uv run pre-commit install
```

## 🧪 Verification

Run the full test suite and linting checks to ensure everything is working:

```bash
# Run all pre-commit hooks on all files
uv run pre-commit run --all-files

# Run tests (if pytest is configured)
uv run pytest
```

## 🔑 Environment Variables

Copy `.env.example` to `.env` and populate necessary keys:

```bash
cp .env.example .env
```

| Variable | Description |
| --- | --- |
| `OPENAI_API_KEY` | (Optional) For AI scripts using OpenAI models. |
| `ANTHROPIC_API_KEY` | (Optional) For AI scripts using Claude models. |
