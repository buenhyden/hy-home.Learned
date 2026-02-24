# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add new AI assistant rules covering Python web scraping, data science, scientific computing, function reflection, Jupyter, and FastAPI development.
- Add new Cursor rules for Python function reflection and FastAPI microservices development.
- Initialize project structure, add TIL notebooks, and migrate dependency management from Poetry to uv.
- Update Renovate configuration to use `uv` and `pep621` managers, enable lock file maintenance, disable Docker and Python updates, and downgrade Python to 3.13.
- Add Python data agent rules and workflows, and directory placeholders.
- Add general Python development rules.
- Add comprehensive Python general rules and best practices documentation.
- Introduce core project documentation and standardize agent rule paths to `.agent/rules`.
- Establish comprehensive project governance, documentation, and automated development workflows.
- Introduce GitHub Actions CI pipeline for quality checks and add new TIL notebooks for Kafka and ipaddress.
- Add new TIL notebooks covering Kafka producer, ipaddress package, and Hugging Face text generation.
- Add GitHub Actions CI workflow for linting, quality checks, and testing.
- Add Jupyter Notebook for Kafka cluster metadata and topic management.
- Add TIL entry for Fernet key generation and update AGENTS.md links to relative paths.
- Implement GitHub Actions CI for linting, formatting, type checking, and testing, while adjusting pre-commit hooks by removing redundant checks.
- Add Kafka cluster smoke test and topic creation utility notebook.
- Add a Kafka smoketest Jupyter notebook to verify cluster functionality.
- Add .editorconfig and .markdownlintignore to standardize code style and exclude files from markdown linting.
- Introduce CI workflow, PR labeler, and enhance pre-commit checks with new linters and schema validations.
- Add GitHub issue template configuration, Dependabot automation, and a CI workflow for quality checks.
- Introduce a comprehensive set of agent rules, workflows, documentation, and templates, while updating core project files.
- Establish repository governance, automation, and issue management with new workflows, policies, and YAML templates, while updating core documentation and configurations.
- Implement automated changelog generation using git-cliff and a GitHub Actions workflow.
- Add mypy, pip-audit, and pytest pre-commit hooks.

### Documentation

- **github:** Update .github assets and expand root README
- **root:** Update root configuration and AI documentation
- Refine root README for better navigation and AI focus
- **readme:** Fix typos and update python version requirement to 3.13+
- **readme:** Deep dive update to match workspace structure and add uv instructions
- Initialize docs folder with guide, structure, and workflow documentation
- **github:** Rename README.md to GITHUB_GUIDE.md for better clarity
- Refactor project documentation by deleting specific AI guides, rewriting the README, and adding contribution guidelines, alongside general project and dependency updates.
- Remove obsolete API references section from README.

### Miscellaneous

- Update Renovate configuration
- **deps:** Update python docker tag to v3.14
- Add agent rules and GitHub templates
- Ignore and untrack .agent/ directory
- **agent:** Track README and workflows, ignore rules
- **git:** Ignore and remove .github agent, prompt, and instruction files
- **github:** Add documentation issue template
- **project:** Update lint config and add .github documentation
- **root:** Refine configuration files, bump version to 0.1.1, and fix pyproject.toml issues
- **github:** Update templates, workflows, and health files for 2026 workspace context
- **deps:** Bump python-multipart in the uv group across 1 directory
- **deps:** Bump pypdf in the uv group across 1 directory
- **deps:** Bump the actions group with 3 updates
- Make pywin32 dependency platform-specific by adding a Windows platform marker.
- Remove typos pre-commit hook
- **deps:** Bump protobuf in the uv group across 1 directory
- **deps:** Bump pip in the uv group across 1 directory
- Add .mypy_cache and .ruff_cache to .gitignore.
- Update multiple package versions, remove anthropic, and enhance platform-specific dependency resolution in uv.lock.chore: Update multiple package versions, remove anthropic, and enhance platform-specific dependency resolution in uv.lock.
- **deps:** Bump cryptography in the uv group across 1 directory
- **deps:** Bump langchain-core in the uv group across 1 directory
- **release:** Update CHANGELOG.md [skip ci]


