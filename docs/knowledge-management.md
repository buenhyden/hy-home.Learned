# 🧠 Knowledge Management Strategy

This document outlines how information flows through the `hy-home-learned` workspace to become permanent knowledge.

## 🌊 The Information Pipeline

We follow a 3-stage pipeline to transform raw data into wisdom.

### Stage 1: Ingestion (`References/`)

- **Status**: Raw, Unprocessed, External.
- **Content**: PDFs, copied lecture notes, massive datasets.
- **Action**: Store in `References/` with clear categorization.
- **Goal**: "Don't lose valid inputs."

### Stage 2: Synthesis (`TIL/`)

- **Status**: Processed, Atomic, Internalized.
- **Content**: "Today I Learned" nodes.
- **Format**: Markdown files in `TIL/YYYY/MM/`.
- **Action**: Read a Reference -> Write a summarized code example or concept in `TIL`.
- **Goal**: "Prove I understand this."

### Stage 3: Systematization (`docs/` & `Code`)

- **Status**: Standardized, Permanent, Referenceable.
- **Content**: Architectural decisions, best practices, reusable libraries.
- **Action**: Detect patterns in multiple `TIL`s -> Promote to a Rule or a Library.
- **Goal**: "Make this the standard."

## 🏷️ Naming & Categorization

- **TIL**: `YYYY-MM-DD-topic-name.md`
- **References**: Keep original names or descriptive slug-case.
- **Tags**: Use `#hashtags` in markdown for cross-linking.

## 🧹 Maintenance

- **Weekly**: Review `TIL` entries.
- **Monthly**: Archive old `task.md` items.
- **Quarterly**: Refactor `References` to remove unused bulk.
