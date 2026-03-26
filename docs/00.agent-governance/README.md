# AI Agent Governance Hub

This directory is the canonical governance hub for AI agents in this repository.

## Directory Structure

- `rules/`: bootstrap, checklist gates, persona routing, documentation protocol, quality checks
- `scopes/`: task-layer instructions by execution domain
- `providers/`: provider-specific runtime notes for Claude and Gemini
- `memory/`: optional reusable memory templates

## Mandatory Load Order

1. Start from repository root `AGENTS.md`.
2. Read `rules/bootstrap.md`.
3. Complete `rules/pre-task-checklist.md`.
4. Select persona in `rules/persona.md`.
5. Load one matching scope file from `scopes/`.
6. Load provider note from `providers/` only if runtime behavior is relevant.

## Matrix And Validation Entry Points

- Use `rules/docs-lifecycle-matrix.md` for a unified `00~11` docs stage contract.
- Use `rules/path-validation.md` to validate stale paths and broken references.
- Use `rules/quality-standards.md` as the final completion gate for governance work.

## Compliance Rules

- Anchor implementation or documentation changes to `docs/01.prd/` or `docs/04.specs/`.
- Track execution in `docs/05.plans/`.
- Keep active governance documents in this directory English-only.
- Update affected README files when navigation, structure, or responsibilities change.

## Language Policy

- Human-facing root guidance: Korean
- AI-facing governance and technical operating docs: English

---
_Last Updated: 2026-03-26_
