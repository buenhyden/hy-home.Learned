# AI Agent Bootstrap

> **layer:** agentic

This file is the repository-wide bootstrap for all coding agents.

## Governance Rules

- Read [docs/README.md](./docs/README.md) first and load only the specific index or document needed for the current task.
- Every code or documentation change must anchor to a requirement in `docs/01.prd/` or a contract in `docs/04.specs/`, and execution must be tracked in `docs/05.plans/`.
- Select the persona and scope that match the task before acting.
- Use the most effective available skills and tools. No artificial whitelist is allowed.
- Update affected README files when structure, responsibilities, or navigation change.

## Documentation Taxonomy

- `docs/00.agent-governance/`: AI-agent governance, routing, provider notes
- `docs/01.prd/`: product requirements
- `docs/02.ard/` and `docs/03.adr/`: architecture references and decisions
- `docs/04.specs/`: technical contracts and design
- `docs/05.plans/`: execution plans
- `docs/06.tasks/`: task tracking
- `docs/07.guides/` to `docs/11.postmortems/`: guides, ops, runbooks, incidents, lessons

## Language Strategy

- Human-facing repository overviews and root guides are written in Korean.
- AI-facing governance and technical operating documents are written in English.
- `docs/00.agent-governance/` must remain English-only.

## Persona And Scope Activation

- Start with `docs/00.agent-governance/rules/bootstrap.md`.
- Load `docs/00.agent-governance/rules/persona.md` to select the task persona.
- Load the matching file in `docs/00.agent-governance/scopes/` for task-specific rules.

## Runtime Handoff

- Claude Code: [CLAUDE.md](./CLAUDE.md)
- Gemini CLI: [GEMINI.md](./GEMINI.md)

## Verification Mandate

- Run the checks required by the touched files and the governing instructions after edits.
- For governance refactors, verify structure, stale paths, language policy, and provider import chains.

---
_Last Updated: 2026-03-26_
