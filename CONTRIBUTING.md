# Contributing to hy-home-learned

Thank you for contributing to this Personal Knowledge Operating System.
This repository is not just code; it is a live knowledge base.

## 🌟 The "Golden Rule"

> **Every commit must either ADD knowledge (TIL/Reference) or IMPROVE the system (Infra/Docs).**

## 🚀 How to Contribute

### 1. Adding Knowledge (TIL)

1. Create a branch: `knowledge/topic-name`.
2. Write your note in `TIL/YYYY/MM/YYYY-MM-DD-topic.md`.
3. Ensure it is atomic and links to at least one Reference or existing TIL.
4. Commit: `docs: add TIL about [topic]`.

### 2. Adding Code / Experiments

1. Create a branch: `feat/experiment-name`.
2. Place code in a relevant directory (or `TIL` if it's a snippet).
3. Ensure strict typing (`mypy`) and linting (`ruff`).
4. Run tests: `uv run pytest`.

### 3. Improving Documentation

1. Create a branch: `docs/improvement`.
2. Update files in `docs/`.
3. **Verify**: Check that `docs/index.md` links remain valid.

## 🛠️ Development Workflow

We use `uv` for all dependency management.

```bash
# Setup
uv sync

# Quality Check
uv run pre-commit run --all-files
```

## ⚖️ Standards

All contributions must adhere to the **[Agent Protocols](docs/agent-protocols.md)** and **[Governance](docs/governance.md)**.
