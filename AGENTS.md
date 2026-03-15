# AI Agent Master Guide

> **layer:** agentic

This document is the authoritative entrypoint for ALL AI assistants as of March 2026.

## 1. Governance Rules

- **Lazy Loading**: Read indices first (`docs/README.md`); load only specific files needed for the task.
- **Skill Autonomy**: You are NOT restricted to specific tool whitelists. Choose the most effective tool for the task.
- **Traceability**: Every code change MUST link to a requirement in `docs/prd/` or a contract in `docs/specs/`.

## 2. Navigation Hierarchy

- **Requirements**: [PRDs](docs/prd/)
- **Decisions**: [ADRs](docs/adr/) | [ARDs](docs/ard/)
- **Operations**: [Incidents](docs/operations/incidents/) | [Runbooks](docs/runbooks/) | [Postmortems](docs/operations/postmortems/)
- **Execution**: [Plans](docs/plans/) | [Specs](docs/specs/)

## 3. Runtime Selection

After reading this guide, immediately load your specific runtime context:

- [Claude Code](CLAUDE.md)
- [Gemini](GEMINI.md)

---
_Last Updated: 2026-03-15_
