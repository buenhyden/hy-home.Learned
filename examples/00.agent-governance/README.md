# AI Agent Governance Hub

Welcome to the central governance directory for AI Agents. This folder defines the rules, scopes, and protocols for all automated and assisted development tasks.

## Directory Structure

- `rules/`: Universal core governance, persona mapping, and repository-wide standards.
  - `bootstrap.md`: The master entry point for all agents.
  - `standards.md`: Universal technical rules and language protocols.
  - `persona.md`: AI Agent persona activation protocols.
  - `git-workflow.md`: Standardized branching and commit protocols.
  - `documentation-protocol.md`: Rules for README synchronization and templates.
- `scopes/`: Layer-specific technical instructions and constraints (Product, Arch, Frontend, Backend, Infra, Security, QA, Docs).
- `providers/`: Tool-specific configurations (Claude Code, Gemini CLI).

## Usage

Agents MUST start with `AGENTS.md` (or provider-specific files like `CLAUDE.md`/`GEMINI.md`) in the root to understand the **Identity Protocol**, then load the matching fragments from this directory JIT (Just-In-Time).

## Compliance

All work must be anchored to `docs/01.prd/` and `docs/04.specs/`. Refer to `rules/standards.md` for detailed compliance requirements.

## 1. 언어 및 운영 원칙 (Language Strategy)

에이전트의 사고 효율성과 사용자의 편의성을 모두 잡기 위해 다음과 같은 이원화 전략을 사용합니다.

- **내부 지침 (Internal Docs)**: AI 에이전트가 직접 읽고 실행하는 규칙(`Rules`, `Scopes`, `Providers`)은 무조건 **English**로 작성합니다. 이는 모델의 추론 성능을 극대화하고 토근 사용량을 최적화하기 위함입니다.
- **사용자 가이드 (User-Facing)**: 인간이 읽는 `README.md` 및 개요 문서는 **한국어(Korean)**로 핵심 지침을 제공합니다.
- **응답 원칙 (Response Mandate)**: 에이전트가 내부적으로 어떤 언어를 사용하든, 사용자와의 대화는 항상 **한국어**로 진행합니다.

## 2. 지능형 지연 로딩 (Lazy Loading Protocol - JIT)

모든 문서를 한꺼번에 읽는 것은 비효율적입니다. 에이전트는 필요한 순간에만 필요한 정보를 로드하는 **Just-In-Time (JIT)** 전략을 따릅니다.

1. **의도 파악 (Intent Identification)**: 요청받은 작업의 성격을 먼저 조치합니다.
2. **부트스트랩 (Bootstrap)**: [rules/bootstrap.md](rules/bootstrap.md)를 통해 기본 분류 체계와 거버넌스를 확인합니다.
3. **규칙 트리거 (Trigger Rule)**: [persona-matrix.md](rules/persona-matrix.md)를 통해 페르소나와 필수 규칙을 로드합니다.
4. **스코프 로딩 (Scope Loading)**: 작업 레이어에 맞는 상세 지침을 [scopes/](scopes/)에서 동적으로 로드합니다.
5. **맥락 메모리 (Contextual Memory)**: [memory/](memory/)에서 과거의 교훈을 탐색합니다.
6. **실행 (Execute)**: 01~11 단계의 SSoT 및 [commands.md](commands.md)를 활용하여 작업을 완성합니다.

## 3. Implementation Flow

### Gateway Dispatcher (JIT Context)

Use the following JIT loading markers to ingest task-specific context from the documentation taxonomy:

| Marker | Target README | Intent |
| :--- | :--- | :--- |
| `[LOAD:PRD]` | `docs/01.prd/README.md` | Requirements & Vision |
| `[LOAD:ARD]` | `docs/02.ard/README.md` | Architecture Reference |
| `[LOAD:ADR]` | `docs/03.adr/README.md` | Technical Decisions |
| `[LOAD:SPECS]` | `docs/04.specs/README.md` | Technical Specifications |
| `[LOAD:PLANS]` | `docs/05.plans/README.md` | Implementation Plans |
| `[LOAD:TASKS]` | `docs/06.tasks/README.md` | Task Tracking |
| `[LOAD:GUIDES]` | `docs/07.guides/README.md` | Developer Guides |
| `[LOAD:OPS]` | `docs/08.operations/README.md` | Operational Policy |
| `[LOAD:RUNBOOKS]` | `docs/09.runbooks/README.md` | Execution Runbooks |
| `[LOAD:INCIDENTS]` | `docs/10.incidents/README.md` | Incident Tracking |
| `[LOAD:POSTMORTEMS]` | `docs/11.postmortems/README.md`| Lessons Learned |

### Specialized Rule Dispatcher

| Strategy | Rule File | Dispatcher Marker |
| :--- | :--- | :--- |
| **Core Governance** | `rules/bootstrap.md` | `[LOAD:RULES:BOOTSTRAP]` |
| **Persona Matrix** | `rules/persona-matrix.md` | `[LOAD:RULES:PERSONA]` |
| **Language Policy** | `rules/language-policy.md` | `[LOAD:RULES:LANG]` |
| **Git Workflow** | `rules/git-workflow.md` | `[LOAD:RULES:GIT]` |
| **README Policy** | `rules/readme-policy.md` | `[LOAD:RULES:README]` |
| **Quality Standards** | `rules/quality-standards.md` | `[LOAD:RULES:QUALITY]` |

## 4. Operational Procedures

### Technical Scopes (Layer Map)

Agents MUST load the corresponding scope from `scopes/` before performing work in a specific layer:

- **Architecture**: `scopes/architecture.md` (`[LOAD:RULES:ARCH]`)
- **Backend**: `scopes/backend.md` (`[LOAD:RULES:BACKEND]`)
- **Frontend**: `scopes/frontend.md` (`[LOAD:RULES:FRONTEND]`)
- **Infrastructure**: `scopes/infra.md` (`[LOAD:RULES:INFRA]`)
- **Mobile**: `scopes/mobile.md` (`[LOAD:RULES:MOBILE]`)
- **Product**: `scopes/product.md` (`[LOAD:RULES:PRODUCT]`)
- **QA**: `scopes/qa.md` (`[LOAD:RULES:QA]`)
- **Security**: `scopes/security.md` (`[LOAD:RULES:SECURITY]`)
- **Ops**: `scopes/ops.md` (`[LOAD:RULES:OPS]`)
- **Docs**: `scopes/docs.md` (`[LOAD:RULES:DOCS]`)
- **Common**: `scopes/common.md` (`[LOAD:RULES:COMMON]`)
- **Entry**: `scopes/entry.md` (`[LOAD:RULES:ENTRY]`)
- **Meta**: `scopes/meta.md` (`[LOAD:RULES:META]`)
- **Agentic**: `scopes/agentic.md` (`[LOAD:RULES:AGENTIC]`)

## 5. Maintenance & Safety

- **Updating Governance**: All changes to files in this directory must be documented in an ADR if they significantly alter agent behavior or repository taxonomy.
- **Validation**: Ensure any changes to dispatcher markers are reflected in root shims.
