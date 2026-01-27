# Agent Rules Index

This index categorizes the 29+ technical rule sets stored in [`.agent/rules/`](file:///d:/hy-home.SourceCode/hy-home.Learned/.agent/rules),
which govern the behavior and reasoning of AI personas within this workspace.

## 🏗️ Core & Architectural Standards

- **0000-Agents**: Persona definitions and basic protocols.
- **0100-Standards**: Foundational architecture, coding style, and governance.
- **1900-Architecture_Patterns**: Specialized design patterns (CQRS, Hexagonal, etc.).

## 🐍 Python & Backend Engineering

- **1100-Python**: Core Python standards and `uv` usage.
- **0900-Backend**: General backend protocols.
- **2000-API_Governance**: REST, GraphQL, and specialized API contracts.
- **0600-DB_and_Data**: SQL, NoSQL, and migration integrity.

## 🤖 AI, Machine Learning & Data

- **0500-AI_and_ML**: LLM orchestration and model interaction.
- **0200-Workflows**: Tool-specific automation logic.

## 🛡️ Stability & Security

- **0700-Testing_and_QA**: AAA patterns, coverage, and reliability.
- **2200-Security**: OWASP compliance and secret management.
- **2300-Performance**: Latency measurement and optimization.

## 🌍 Web & Frontend

- **0800-Web_Development**: General web standards.
- **1700-React**, **1200-Nextjs**: Framework-specific best practices.
- **1500-Typescript**, **1600-Javascript**: Scripting language standards.

## 📦 DevOps & Infrastructure

- **0300-DevOps_and_Infrastructure**: Deployment and local env management.
- **0400-Cloud**: AWS, GCP, and cloud-native governance.

---

## Usage Instructions for AI

Agents should cross-reference a task's domain with this index to identify the specific `0XXX-standard.md`
rules they MUST follow during execution.
