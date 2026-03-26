# Documentation Protocol

This protocol defines how human-facing and AI-facing documents must be maintained.

## Language Policy

- Root repository guidance is written in Korean.
- AI-facing governance and technical operating documents are written in English.
- `docs/00.agent-governance/` must remain English-only.

## README Synchronization

- Update `README.md` when the repository structure, navigation, or language contract changes.
- Update `docs/00.agent-governance/README.md` when the governance tree or file responsibilities change.
- README files must describe the final completed structure, not a transitional state.

## Template Usage

- Use `docs/99.templates/` when creating new governed documents.
- Use relative links only.
- Remove placeholders before saving.

## Scope Hygiene

- Do not duplicate repository-wide standards inside provider notes.
- Do not create alternate top-level governance maps outside the numeric docs taxonomy.
