# Claude Code Runtime File

> **layer:** agentic

This file initiates the Claude Code runtime environment (March 2026 Edition).

## Runtime Activation

You MUST lazily load the following layers upon session initialization:

1. [Shared Governance](docs/agentic/shared/shared-governance.md)
2. [Operating Guide](docs/agentic/shared/repository-guide.md)
3. [Claude Overlay](docs/agentic/shared/claude-code.md)

## Skill Policy

Skill usage is governed purely by intent and task suitability. Refer to [Claude Overlay](docs/agentic/shared/claude-code.md#skills) for guidance. No artificial tool whitelists are enforced; agents must exercise greedy autonomy to fulfill user requests efficiently.

---
@./docs/agentic/shared/shared-governance.md
@./docs/agentic/shared/repository-guide.md
@./docs/agentic/shared/claude-code.md
