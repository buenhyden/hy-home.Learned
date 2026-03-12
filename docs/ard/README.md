# Architecture Reference Documents (ARD)

This directory contains Architecture Reference Documents that define the high-level structural models and global behavioral flows of the `hy-home-learned` ecosystem.

## 1. Role in Documentation Hierarchy

ARDs serve as the structural blueprint for the system. They provide the "How it works globally" context, sitting between high-level requirements and low-level source code.

- **Upstream**: [**docs/prd/**](../prd/) (Requirements) -> [**docs/adr/**](../adr/) (Decisions)
- **Mapping**: Adheres to [**Architecture Design Standards**](../../.agent/rules/0130-architecture-standard.md).

## 2. Navigation Protocol (Lazy Loading)

AI Agents MUST follow the **Lazy Loading** pattern defined in [**AGENTS.md**](../../AGENTS.md):

1. Use this `README.md` to find the relevant domain or system diagram.
2. Load only the specific ARD file required for the current task (e.g., `ard/data-model.md`).

## 3. Reference Standards

Documents here MUST contain:

- **Structural Diagrams**: C4 Model (Context, Container) preferred.
- **Domain Models**: Entity relationships and core logic flows.
- **Cross-Links**: Direct links to governing ADRs and downstream Specs.

## 4. Index of References

| System / Domain | Title | Status | Last Updated |
| :--- | :--- | :--- | :--- |
| - | _No ARDs yet_ | - | - |

---
_Last Updated: March 2026_
                                         |
| ------------------------------- | ----------------------------------------------- |
| **Introduction**                | High-level overview                             |
| **Business Goals**              | Top-level objectives                            |
| **Scope**                       | System boundaries                               |
| **Functional Requirements**     | Core technical capabilities                     |
| **Constraints**                 | External limitations                            |

## Key Sections

### Non-Functional Requirements (NFRs)

NFRs are critical for ARDs. Document:

- **Performance**: Latency, throughput, response times
- **Scalability**: Load projections, scaling strategy
- **Reliability**: Uptime SLA, RTO/RPO
- **Security**: Encryption, compliance, authentication
- **Observability**: Logging, metrics, tracing

### Constraints

Document factors that limit architectural choices:

- Budget limitations
- Technology constraints
- Team expertise
- Regulatory compliance
- Legacy system integration

## Relationship to Other Documents

```text
[Business Need]
      ↓
docs/prd/ (What - Product Requirements)
      ↓
docs/ard/ (How - Architecture Requirements, validated via 6 Core Engineering Pillars)
      ↓
docs/adr/ (Why - Architecture Decisions)
      ↓
specs/ (Implementation Specifications)
```

## AI Agent Guidelines

When working with ARDs:

1. **Read before designing**: Check existing ARDs in the relevant domain folders for requirements
2. **Use template**: Always use `templates/architecture/ard-template.md`
3. **Be specific**: Quantify NFRs (e.g., "99.9% uptime" not "high availability")
4. **Link to ADRs**: Reference relevant ADRs in constraints section
5. **Pillar Validation**: Validate that ARDs align with `.agent/rules/1910-architecture-documentation.md` and account for the 6 Core Engineering Pillars (Security, Observability, Performance, Compliance, Documentation, Localization).

## Index of ARDs

| Document | System        | Last Updated |
| -------- | ------------- | ------------ |
| -        | _No ARDs yet_ | -            |

> Add entries to this index as ARDs are created.
