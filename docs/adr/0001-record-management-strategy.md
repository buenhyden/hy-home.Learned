# ADR 0001: Record Management Strategy

## Status

Proposed / Accepted (2026-01-27)

## Context

As a personal knowledge workspace, `hy-home-learned` accumulates a vast amount of diverse information
(code, lecture notes, textbook summaries, AI rules). Without a clear management strategy, the repository
risks becoming fragmented and unsearchable for both humans and AI agents.

## Decision

We will adopt a **Dual-Axis Organization Strategy**:

1. **Temporal Axis (`TIL/`)**: All personal learnings will be organized by year and month (`YYYY/MM`).
   This allows for tracking professional growth over time.
2. **Thematic Axis (`References/`)**: All external source materials will be organized by category
   (Books, Lectures, Data). This allows for quick context-switching between different study domains.

### Rules for Record Entry

- **TIL nodes** must include a standardized header and at least one code snippet or summary.
- **Reference materials** must be stored in their respective category folder to prevent root-level clutter.
- **AI Rule alignment**: Every directory must be represented in the `directory-inventory.md` for AI traceability.

## Consequences

- **Positive**: High discoverability, clear growth timeline, and seamless AI agent context loading.
- **Negative**: Requires manual categorization effort when adding new notes.
- **Mitigation**: AI Agents (like the Refactoring Lead) can assist in auto-categorizing and summarizing raw notes.
