# DevOps Pillar Standards

> **layer:** agentic
> **Status:** Active
> **Source:** Refactored from `.agent/rules/0300-DevOps_and_Infrastructure/0300-devops-pillar-standard.md`

## 1. Core Principles

- **[REQ-OPS-IMM-01] Immutability**: Servers MUST NOT be patched; replacement only ("Cattle, not Pets").
- **[REQ-OPS-IAC-01] Declarative Infrastructure**: Manual "ClickOps" is strictly FORBIDDEN. All infra is code.
- **[REQ-OPS-OBS-01] Observability-by-Default**: Systems MUST emit Metrics, Logs (JSON), and Traces.

## 2. Configuration & Security

- **[REQ-OPS-CFG-01] External Config**: App config MUST be injected via ENV or secret stores.
- **[REQ-OPS-SEC-01] Secret Management**: NEVER commit secrets to git. Use Vault, KMS, or GitHub Secrets.

## 3. SRE & Reliability

- **[REQ-SRE-SLO-01] SLOs**: Critical services MUST have defined SLIs/SLOs (e.g., 99.9% availability).
- **[REQ-SRE-ERR-01] Error Budgets**: Deployments MUST halt if budgets are exhausted.
- **[REQ-OPS-DOC-01] Deterministic Images**: Use specific tags (no `latest`).
- **[REQ-OPS-DOC-02] Non-Root Execution**: Containers MUST NOT run as root.

## 4. Lifecycle Procedures

1. Code -> 2. Plan/Diff -> 3. Policy Review -> 4. Automated Apply.
