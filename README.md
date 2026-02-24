# hy-home-learned

<p align="center">

![CI Status](https://github.com/buenhyden/hy-home.Learned/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)

</p>

<p align="center">

**A Personal Knowledge Operating System**
_Optimized for AI-Human Collaboration_

[**Explore Docs**](docs/index.md) • [**View Knowledge**](TIL/) • [**Agent Brain**](.agent/)

</p>

---

## 🚀 Overview

**hy-home-learned** is a structured workspace designed to bridge the gap between "Learning" and "Doing". It integrates proactive AI agents, strict governance (Mypy/Ruff), and a layered architecture to turn raw references into executable knowledge.

### Key Features

- **🤖 Agentic Core**: Built-in personas for Reasoning, Coding, and Reviewing (`.agent/`).
- **🧠 Atomic Knowledge**: "Today I Learned" (TIL) system for verifying understanding.
- **🛡️ Strict Governance**: Automated CI/CD pipelines ensuring code quality.
- **⚡ Modern Stack**: Powered by `uv` for lightning-fast Python management.

## 🧭 Directory Map

| Directory                        | Description                                                          |
| -------------------------------- | -------------------------------------------------------------------- |
| [**`docs/`**](docs/index.md)     | **The Manual**. Start here. Contains Mission, Guides, and Inventory. |
| [**`TIL/`**](TIL/)               | **The Knowledge**. Chronological learning nodes (2024-2026).         |
| [**`References/`**](References/) | **The Library**. Raw external inputs (Books, Lectures).              |
| [**`.agent/`**](.agent/)         | **The Brain**. Governance rules and workflow automation scripts.     |
| [**`.github/`**](.github/)       | **The Pipeline**. CI/CD, Issue Templates, and Automation.            |

## 🛠️ Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv)

### Quick Setup

```bash
# 1. Clone
git clone https://github.com/buenhyden/hy-home.Learned
cd hy-home-learned

# 2. Sync Dependencies
uv sync

# 3. Install Hooks
uv run pre-commit install
```

Detailed instructions in [**Development Setup Guide**](docs/development-setup-guide.md).

## 🤝 Contributing

We welcome contributions that add knowledge or improve wisdom.
Please read [**CONTRIBUTING.md**](CONTRIBUTING.md) and [**Agent Protocols**](docs/agent-protocols.md) before starting.

## 📜 License

Distributed under the MIT License. See [**LICENSE**](LICENSE) for more information.
