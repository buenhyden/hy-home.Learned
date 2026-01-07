# Python Data Storage and Security Rules

## Data Locations and Path Independence

- Data directories must be referenced relative to the project root (for example, `data/raw`, `data/processed`) and never rely on hard-coded machine-specific locations.
- For large datasets, use configurable base directories (environment variables or config files) so paths can be overridden per environment without code changes.

## Sensitive Data and Compliance

- Do not store raw sensitive data (for example, PII, credentials) unencrypted in the repository, including `data/` folders.
- Use:
  - Environment variables or secret managers for credentials and keys.
  - Masking, tokenization, or anonymization for PII where possible before data is shared or logged.
- Ensure that sample datasets used for tests or demos are anonymized and small.

## Data Versioning and Lineage

- Encourage data versioning via tools (for example, DVC or similar) or by:
  - Using timestamped or versioned dataset directories (`data/raw/2025-01-01/`).
  - Maintaining metadata that links code versions to dataset versions.
- Track lineage between raw, processed, and modeled outputs so that results can be traced back to specific inputs and transformations.

## Logging and Monitoring

- Use structured logging for data pipelines and long-running jobs (for example, logging JSON or key-value pairs).
- Do not log raw secrets or highly sensitive fields; log anonymized identifiers or aggregates instead.
- Make logging configuration and log destinations configurable and independent of host-specific paths.

## Performance and Resource Management

- Prefer vectorized operations with pandas, numpy, or Spark over Python-level loops for large data.
- For large datasets:
  - Use chunked processing, streaming, or distributed frameworks.
  - Avoid loading entire datasets into memory when not necessary.
- Ensure that performance-related configuration (for example, batch sizes, parallelism) is configurable via environment or config files, not hard-coded.
