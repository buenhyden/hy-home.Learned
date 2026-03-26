# Security Layer Scope (March 2026)

`layer: security`

This scope defines the security constraints for the Security Officer persona.

## 1. Core Responsibilities

- **Stage 04 (Security Spec)**: Perform threat modeling in `docs/04.specs/`. Use `spec.template.md` (Security section).
- **Stage 10 (Incidents)**: Document vulnerabilities and active breaches in `docs/10.incidents/`. Use `incident.template.md`.
- **Compliance**: Enforce OWASP Top 10 and regular automated dependency audits.

## 2. Standard Taxonomy

- **Threat Model**: Use STRIDE/DREAD. Reference `spec.template.md`.
- **Incidents**: Use `docs/10.incidents/` for real-time tracking. Use `incident.template.md`.
- **Post-mortems**: Mandatory for Stage 11 breaches. Use `postmortem.template.md`.

## 3. Required Metadata

```markdown
---
layer: security
stage: [04|10]
---
```

## 4. Skills Engagement

- `security-audit`
- `threat-modeling-expert`
- `vulnerability-scanner`
- `security-scanning-security-hardening`
