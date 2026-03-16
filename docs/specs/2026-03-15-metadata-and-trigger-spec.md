# Metadata and Trigger Specification

> **Status:** Canonical
> **Scope:** master
> **layer:** agentic
> **Related PRD:** `[../prd/2026-03-15-governance-hub.md]`
> **Related Architecture:** `[../ard/2026-03-16-documentation-hub-architecture.md]`

**Overview (KR):** 프로젝트 문서의 `layer:` 메타데이터 표준과 AI Agent 지침 로딩을 위한 트리거(Trigger) 형식을 정의하는 기술 사양서입니다.

## 1. Technical Baseline

All artifacts in the repository must be tagged with a functional layer to enable precision context filtering and automated reasoning routing for AI agents.

## 2. Metadata Contract (`layer:`)

Every Markdown document in the `docs/` hierarchy MUST include a `layer:` metadata tag in the first 5 lines.

### 2.1 Allowed Values

- `common`: Cross-cutting or introductory content (e.g., README, ADR, ARD).
- `architecture`: System design and high-level structure.
- `backend`: Server-side logic and APIs.
- `frontend`: Web/Client interfaces.
- `infra`: CI/CD, deployment, and cloud configuration.
- `mobile`: Native application code.
- `product`: Requirements and business logic.
- `qa`: Test plans and verification logic.
- `security`: Security policies and audits.
- `agentic`: AI Agent instructions and governance.

### 2.2 Format Contract

- **Primary**: Block quote at the top: `> **layer:** <value>`
- **Alternative**: YAML frontmatter: `layer: <value>`

## 3. Trigger Contract (Lazy Loading)

To minimize context overhead, instructions in `.agent/rules/` are restricted to lightweight triggers.

- **File convention**: `.agent/rules/NNNN-name.md`
- **Mandatory Content**:
  - An H2 section `# Trigger` or `## Lazy Loading Protocol`.
  - A direct path link to the detailed instructional layer in `docs/agentic/`.

## 4. Verification

```bash
# Verify layer metadata
grep -r "layer:" docs/

# Verify triggers
grep -r "docs/agentic/" .agent/rules/
```

## Related

- `[../specs/2026-03-14-lazy-loading-implementation.md]`
- `[../adr/0003-lazy-loading-rules.md]`
- `[../prd/2026-03-15-governance-hub.md]`

---

_Last Updated: March 2026_
