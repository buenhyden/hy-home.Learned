# AI Agent Bootstrap

> **layer:** agentic

Repository-wide bootstrap for all coding agents.

## Core Contract

- Read [docs/README.md](./docs/README.md) first.
- Follow [bootstrap](./docs/00.agent-governance/rules/bootstrap.md) and complete the mandatory [pre-task checklist](./docs/00.agent-governance/rules/pre-task-checklist.md).
- Select persona and scope from [persona routing](./docs/00.agent-governance/rules/persona.md) before implementation.
- Anchor every change to `docs/01.prd/` or `docs/04.specs/`, and track execution in `docs/05.plans/`.
- Keep instructions lazy-loaded: bootstrap -> checklist -> persona -> scope -> provider note.

## Numeric Docs Taxonomy

- `docs/00.agent-governance/`: AI-agent governance
- `docs/01.prd/`: product requirements
- `docs/02.ard/` and `docs/03.adr/`: architecture references and decisions
- `docs/04.specs/`: technical contracts and design
- `docs/05.plans/`: execution plans
- `docs/06.tasks/`: task tracking
- `docs/07.guides/` to `docs/11.postmortems/`: guides, operations, runbooks, incidents, postmortems

## Language Policy

- Human-facing repository guides are written in Korean.
- AI-facing governance and technical operating files are written in English.
- `docs/00.agent-governance/` must remain English-only.

## Provider Entrypoints

- Claude Code: [CLAUDE.md](./CLAUDE.md)
- Gemini CLI: [GEMINI.md](./GEMINI.md)

## Verification Mandate

- Run the checks required by touched files.
- For governance edits, run [path validation](./docs/00.agent-governance/rules/path-validation.md) and [quality standards](./docs/00.agent-governance/rules/quality-standards.md).

---
_Last Updated: 2026-03-26_
