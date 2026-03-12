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

[**Explore Docs**](docs/README.md) • [**View Knowledge**](TIL/) • [**Agent Brain**](AGENTS.md)

</p>

---

## Overview

**hy-home-learned** is a structured workspace designed to bridge the gap
between learning and doing. It combines proactive AI agents, repository
governance, and layered documentation to turn raw references into reusable
knowledge.

### Key Features

- **Agentic Core**: Built-in personas, rules, and workflows under `.agent/`
- **Atomic Knowledge**: A TIL system for verified learning notes
- **Documentation Chain**: Requirements, architecture, specs, plans, and
  runbooks under `docs/`
- **Modern Python Tooling**: `uv`, `ruff`, `mypy`, `pytest`, and `pre-commit`

## Directory Map

| Directory | Description |
| --------- | ----------- |
| [**`docs/`**](docs/README.md) | Documentation hub for requirements, architecture, specs, plans, runbooks, and operations |
| [**`TIL/`**](TIL/) | Chronological knowledge notes |
| [**`AGENTS.md`**](AGENTS.md) | Shared agent entrypoint |
| [**`GEMINI.md`**](GEMINI.md) | Gemini runtime entrypoint |
| [**`CLAUDE.md`**](CLAUDE.md) | Claude Code runtime entrypoint |
| [**`.claude/`**](.claude/README.md) | Shared human-facing agent manuals |
| [**`.agent/`**](.agent/) | Rules, workflows, and automation assets |
| [**`.github/`**](.github/) | CI/CD and repository automation |

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv)

### Quick Setup

```bash
git clone https://github.com/buenhyden/hy-home.Learned
cd hy-home-learned
uv sync
uv run pre-commit install
```

For repository navigation, start with [docs/README.md](docs/README.md) and
[AGENTS.md](AGENTS.md).

## Contributing

We welcome contributions that add knowledge or improve the repository.
Please read [**CONTRIBUTING.md**](CONTRIBUTING.md), [**AGENTS.md**](AGENTS.md),
and [**docs/README.md**](docs/README.md) before starting.

## License

This checkout advertises MIT license terms in repository metadata. If a
published `LICENSE` file is added later, link it here.
