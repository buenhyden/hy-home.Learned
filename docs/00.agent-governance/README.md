# AI Agent Governance Hub

This directory is the canonical governance hub for AI agents working in this repository.

## Directory Structure

- `rules/`: repository-wide bootstrap, persona routing, documentation protocol, git workflow, and quality gates
- `scopes/`: task-layer guidance for product, architecture, backend, docs, infra, ops, security, qa, and meta-governance work
- `providers/`: provider-specific notes for Claude Code and Gemini CLI
- `memory/`: optional memory templates and notes for future reuse

## Usage Order

1. Start from the repository root `AGENTS.md`.
2. Read `rules/bootstrap.md`.
3. Load `rules/persona.md` to select the task persona.
4. Load the matching file from `scopes/`.
5. Load the relevant file from `providers/` when the runtime matters.

## Compliance

- All work must anchor to `docs/01.prd/` or `docs/04.specs/`, with execution tracked in `docs/05.plans/`.
- Read the docs index first and load only the documents needed for the active task.
- Keep active governance files in this directory English-only.
- Update README files when structure, responsibilities, or navigation change.

## Relationship To The Numeric Docs Taxonomy

- `docs/01.prd/`: product intent and requirements
- `docs/02.ard/` and `docs/03.adr/`: architecture references and decisions
- `docs/04.specs/`: technical contracts and implementation design
- `docs/05.plans/`: execution plans
- `docs/06.tasks/`: task tracking
- `docs/07.guides/` to `docs/11.postmortems/`: guides, operations, runbooks, incidents, and lessons learned

## Language Rule

- Human-facing root guidance is written in Korean.
- Active AI-agent governance files in this directory are written in English.

---
_Last Updated: 2026-03-26_
