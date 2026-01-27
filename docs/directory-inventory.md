# 🗺️ Directory Inventory

This document serves as the cartography for the `hy-home-learned` workspace.

## 📂 Root Level

| Directory | Purpose |
| --- | --- |
| [`.agent/`](../.agent) | **The Brain**. Contains `rules` (governance), `skills` (capabilities), and `workflows` (automation). This is the source of truth for AI behaviors. |
| [`.github/`](../.github) | **The Pipeline**. GitHub Actions workflows, Issue templates, and PR templates. |
| [`docs/`](../docs) | **The Manual**. This documentation folder. Contains Mission, Guides, and Inventory. |
| [`References/`](../References) | **Raw Materials**. External knowledge sources. |
| [`TIL/`](../TIL) | **Processed Knowledge**. "Today I Learned" nodes, organized by time. |

## 📚 Knowledge Layer Structure

### `References/`

- **`Books/`**: Notes, summaries, and code from technical books.
- **`Lectures-InFlearn/`**: Course materials from InFlearn.
- **`Online-Lecture-Data/`**: Global MOOC resources (Udemy, Coursera).
- **`Lecture-Data/`**: General lecture notes.
- **`Compression-Files/`**: Archives or large blobs (if necessary).

### `TIL/`

Organized chronologically to capture the learning journey.

- **`2024/`**: Archives from 2024.
- **`2025/`**: Archives from 2025.
- **`2026/`**: Current active learning nodes.

## 🧠 Agent Layer (`.agent/`)

- **`rules/`**: Technical constraints. E.g., `0002-strong-reasoner-agent.md`, `0010-api-design-standard.md`.
- **`skills/`**: Tools and capability definitions for agents.
- **`workflows/`**: Declarative `.md` files that define multi-step processes agents can execute.

## ⚙️ Configuration Files

- **`pyproject.toml`**: The definition of the Python project, dependencies, and tool configs (`ruff`, `mypy`).
- **`uv.lock`**: Exact version lockfile for reproducible builds.
- **`.pre-commit-config.yaml`**: Configuration for git hooks.
