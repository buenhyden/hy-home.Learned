# 🏛️ Project Governance

This document establishes the laws of the repository to ensure long-term health and collaboration.

## 📜 Architectural Decision Records (ADR)

Significant decisions must be recorded.

- **Location**: [`docs/adr/`](./adr/)
- **Format**: [MADR](https://adr.github.io/madr/) (Markdown Architectural Decision Records).
- **Trigger**: When a decision has a significant impact on architecture, workflow, or technology stack.
- **Status**: `Draft` -> `Proposed` -> `Accepted` / `Rejected`.

## 📝 Naming Conventions

| Entity | Casing | Example |
| --- | --- | --- |
| **Files** | `kebab-case` | `my-file-name.md` |
| **Directories** | `kebab-case` (mostly) | `my-folder/` (Exceptions: `TIL`, `References` are specific ProperCase roots) |
| **Python Files** | `snake_case` | `my_module.py` |
| **Python Classes** | `PascalCase` | `MyClass` |
| **Python Vars** | `snake_case` | `my_variable` |

## 🔒 Security & Secrets

- **NEVER** commit secrets (API keys, passwords).
- Use `.env` files (gitignored).
- Use `.secrets.baseline` if using `detect-secrets`.

## 📦 Dependency Management

- All dependencies must be added via `uv`.
- `uv sync` is the source of truth.
- Do not edit `pyproject.toml` dependencies manually if possible; use `uv add`.
