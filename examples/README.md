# Example Implementations

This directory holds sample codes, mock configurations, and proof-of-concept setups demonstrating how to use the templates defined in `/templates/`.

## Purpose

- Provide humans and AI models with tangible references for how specific components or integrations are expected to work in this architecture.
- Isolate experimental code from the primary `/src` and specification paths.

## Available Examples

| Example File           | Template Used         | Purpose                                                  |
| ---------------------- | --------------------- | -------------------------------------------------------- |
| `example-adr.md`       | `adr-template.md`     | Architecture Decision Record for database selection      |
| `example-prd.md`       | `prd-template.md`     | Product Requirements Document for authentication feature |
| `example-runbook.md`   | `runbook-template.md` | Deployment runbook with rollback procedures              |

## Related Examples

- `../specs/example-spec.md` - Complete feature specification example

## Guidelines

- All examples should include brief inline comments explaining their intended context.
- Assume nothing in this folder will be deployed to production.
- Examples follow the exact structure defined in their corresponding templates.

## AI Agent Guidelines

While these serve as "examples" to guide format and structure, any AI agent deriving actual project templates or creating new documents from these MUST ensure full compliance with the latest `.agent/rules/`. An "example" configuration seen here does not override a strict security or operational rule defined in the `.agent/rules/` boundary unless explicitly permitted by `docs/guides/`.
