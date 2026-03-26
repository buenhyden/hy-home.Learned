# AI Agent Master Guide

> **layer:** agentic

This document is the authoritative entrypoint for ALL AI assistants as of March 2026.

## 1. Governance Rules

- **Lazy Loading**: Read indices first (`docs/README.md`); load only specific files needed for the task. Use `list_dir` or `view_file_outline` to discover structure.
- **Skill Autonomy**: You are NOT restricted to specific tool whitelists. Choose the most effective tool for the task based on intent and efficiency.
- **Traceability**: Every code change MUST link to a requirement in `docs/01.prd/` or a contract in `docs/04.specs/` and be tracked in `docs/05.plans/`.

## 2. Navigation Hierarchy

- **Requirements**: [PRDs](docs/01.prd/)
- **Decisions**: [ADRs](docs/03.adr/) | [ARDs](docs/02.ard/)
- **Operations**: [Incidents](docs/10.incidents/) | [Runbooks](docs/09.runbooks/) | [Postmortems](docs/11.postmortems/)
- **Execution**: [Plans](docs/05.plans/) | [Specs](docs/04.specs/)

## 3. Runtime Selection

After reading this guide, immediately load your specific runtime context:

- [Claude Code](CLAUDE.md)
- [Gemini](GEMINI.md)

---
_Last Updated: 2026-03-15_
