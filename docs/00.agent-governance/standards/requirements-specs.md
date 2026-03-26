# Requirements & Specifications Standards

> **layer:** agentic
> **Status**: Active
> **Source**: Refactored from `.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md`

- **Role**: Product Owner / Lead Engineer
- **Purpose**: Define standard formats for PRDs and Specifications to ensure alignment on "What" is being built.

## 1. Product Requirements Document (PRD)

Mandatory sections for `docs/prd/`:

- **Context**: Problem statement and user needs.
- **User Stories**: Functional requirements from the user's perspective.
- **Success Metrics**: How we measure the impact of the change.
- **Constraints**: Technical or business limitations.

## 2. Technical Specifications

Mandatory sections for `docs/specs/`:

- **API Definition**: Exact endpoint or interface signatures (e.g., OpenAPI).
- **Data Model**: Schema changes or new entities.
- **Security**: Authentication and authorization requirements.
- **Error Handling**: Standard error codes and recovery paths.

## 3. Mandatory Protocols

- **[REQ-SPE-01] No Placeholder Specs**: Never start development with a "TBD" specification.
- **[REQ-SPE-02] Template Compliance**: Use the official project templates.

## 4. Validation Criteria

- [ ] PRD exists for the feature.
- [ ] Spec is approved before code implementation begins.
