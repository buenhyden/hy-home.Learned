# API Design Standards

> **layer:** agentic
> **Status**: Active
> **Source**: Refactored from `.agent/rules/0000-Agents/0010-api-design-standard.md`

- **Role**: REST & GraphQL Architect
- **Purpose**: Define standards for the creation, evolution, and documentation of scaled API interfaces.

## 1. Core Principles

- **[REQ-API-01] Resource-Oriented Modeling**: Paths MUST use plural nouns (e.g., `/users`). Verbs are prohibited.
- **[REQ-API-02] Versioning Discipline**: Use explicit versioning in URL paths (e.g., `/v1/`).
- **[REQ-API-03] Normalized Errors**: Consistent HTTP status codes and machine-readable error payloads.

## 2. Modeling & Documentation

- **OpenAPI**: Mandatory for REST APIs.
- **SDL**: Mandatory for GraphQL.
- **Template**: Always follow `templates/api-spec-template.md`.

## 3. Security & Validation

- **RBAC**: Enforced at the gateway or middleware level.
- **Input Validation**: Strict schema enforcement (JSON Schema, Pydantic).

## 4. Validation Criteria

- [ ] OpenAPI spec accurately reflects 100% of endpoint behavior.
- [ ] Zero endpoint paths utilize verbs.
- [ ] No sensitive fields exposed in JSON payloads.
