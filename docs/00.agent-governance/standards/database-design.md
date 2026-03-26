# Database Design Standards

> **layer:** agentic
> **Status**: Active
> **Source**: Refactored from `.agent/rules/0000-Agents/0011-database-design-standard.md`

- **Role**: Principal Data Architect
- **Purpose**: Define standards for scalable, performant, and normalized data schemas.

## 1. Normalization & Keys

- **[REQ-DBA-01] 3NF Baseline**: Relational schemas default to Third Normal Form.
- **[REQ-DBA-02] Primary Keys**: Mandatory UUID or BigInt keys.

## 2. Migration Integrity

- **[REQ-DBA-03] Reversible Migrations**: Every migration MUST have balanced `UP` and `DOWN` logic.
- **Narrative Naming**: Files follow `YYYYMMDD_description.sql` pattern.

## 3. Performance & Safety

- **Indexing**: Foreign keys MUST have associated indexes.
- **Soft Deletes**: Use `deleted_at` for critical business data.
- **Explain Analyze**: Mandatory for query-heavy schema changes.

## 4. Validation Criteria

- [ ] New schemas adhere to 3NF unless denormalization is documented.
- [ ] `DOWN` script restores state without data loss.
- [ ] Zero orphaned records possible due to constraints.
