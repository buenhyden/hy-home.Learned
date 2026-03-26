# Documentation Protocol

This protocol defines language, lifecycle, and synchronization rules for repository documentation.

## Language Policy

- Human-facing overview documentation is written in Korean.
- AI-facing governance and technical operating documents are written in English.
- `docs/00.agent-governance/` must remain English-only.

## Immutable Content Guardrail

- Do not rewrite existing authored content under `docs/01~99/` unless explicitly requested by a human owner.
- Governance improvements should be implemented through `docs/00.agent-governance/` and root entrypoint updates.

## Lifecycle Contract

- Use `docs-lifecycle-matrix.md` as the unified stage contract for `00~11`.
- Use stage README files as source truth for purpose and template mapping.

## README Synchronization

- Update root `README.md` when repository navigation or language policy changes.
- Update `docs/README.md` when taxonomy navigation changes.
- Update `docs/00.agent-governance/README.md` when governance routing changes.
- README files must describe the final completed state, not transitional state.

## Template Usage

- Use `docs/99.templates/` for new documents.
- Use relative links for cross-references.
- Remove placeholders before completion.

## Scope Hygiene

- Keep repository-wide standards in `rules/`.
- Keep provider-specific behavior in `providers/`.
- Do not duplicate global standards across provider files.
