# System Architecture

> **layer:** architecture

This document defines the high-level architecture of projects created from this template. It serves as a blueprint that should be customized for each new project.

## 1. System Context

This template provides a standardized foundation for building spec-driven, agent-governed projects.

### Core Architecture Pillars

- **Spec-Driven Development**: All code implementation is driven by verified specifications.
- **AI-Assisted Governance**: A multi-agent system manages documentation and operations.
- **Boundary Segregation**: Knowledge (`docs/`), Implementation (`docs/specs/`, modules), and Operations (`docs/operations/`).

## 2. Core Constraints & Decisions

### Core Constraints & Decisions

| Decision                | Rationale                                                                         |
| ----------------------- | --------------------------------------------------------------------------------- |

> See `docs/adr/` for detailed Architecture Decision Records that shaped this specific system logic. Each ADR is tagged with its functional `layer:`.

## 3. Architecture & Tech Stack Checklist

When starting a project or writing an Architecture Reference Document (ARD), the following checklist MUST be addressed and agreed upon by the Human and Planner Agent:

| Category                  | Check Question                                                                                                                                                                 | Priority      | Notes / Decisions     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | --------------------- |
| **Architecture Style**    | Is the architectural style decided (e.g., Monolithic, Modular Monolith, Microservices)?                                                                                        | **Mandatory** |                       |
| **Service Boundaries**    | Are the boundaries and responsibilities of core services/modules expressed in diagrams/docs?                                                                                   | **Mandatory** |                       |
| **Domain Model**          | Are core domain entities (e.g., User, Document) and relations defined (ER/UML)?                                                                                                | **Mandatory** |                       |
| **Tech Stack (Backend)**  | Have the language, framework, and key libraries (e.g., web framework, ORM) been decided?                                                                                       | **Mandatory** |                       |
| **Tech Stack (Frontend)** | Have the framework (React/Vue/Next), state management, and build tools been decided?                                                                                           | **Mandatory** |                       |
| **Database**              | Have the primary DB engine (e.g., MySQL, PostgreSQL, MongoDB) and schema strategy been decided?                                                                                | **Mandatory** |                       |
| **Messaging / Async**     | Is a message broker (e.g., Kafka, RabbitMQ) or async processing method defined?                                                                                                | _Optional_    |                       |
| **Infrastructure**        | Is the deployment target (Cloud/On-Prem, Kubernetes, Serverless) decided?                                                                                                      | **Mandatory** |                       |
| **Non-Functional Req**    | Are NFRs (Availability, Latency, Throughput) defined with quantitative metrics?                                                                                                | **Mandatory** |                       |
| **Scalability Strategy**  | Are Scale-up/out, partitioning, or caching strategies drafted?                                                                                                                 | _Optional_    |                       |
| **Arch. Principles**      | Is there a documented list of architectural principles, including "what NOT to do"?                                                                                            | _Optional_    |                       |
| **ADR Management**        | Is there a process established to leave ADRs for key technical decisions?                                                                                                      | _Optional_    | Yes, use `docs/adr/`. |
| **Pillar Alignment**      | Does the architecture align with the 6 Core Pillars (Security `2200`, Performance `2300`, Observability `2600`, Compliance `2400`, Documentation `2100`, Localization `2500`)? | **Mandatory** | See `.agent/rules/`.  |
| **Agent Rule Compliance** | Does the tech stack selection comply with language/framework specific laws (e.g., `1200-Nextjs.md`) defined in `.agent/rules/`?                                                | **Mandatory** |                       |

> **Process Enforcement**: The Planner Agent MUST explicitly answer all items of this checklist when creating an ARD, adhering to `docs/agentic/standards/architecture-standards.md`. The Reviewer Agent MUST verify that any code changes do not violate these decisions before merging. All documents MUST include the `layer:` metadata.

## 4. Reference Technology Stack (Template)

Customize the following for your specific project upon cloning.

| Layer        | Recommended Technology        | Purpose                    |
| ------------ | ----------------------------- | -------------------------- |
| **Frontend** | React / Next.js / TailwindCSS | Client-side interactions   |
| **Backend**  | Node.js / Python / Go / Rust  | Server-side APIs and logic |
| **Database** | PostgreSQL / MongoDB          | Data persistence           |
| **DevOps**   | Docker / GitHub Actions       | CI/CD and Containerization |

## 4. Integration & Separation Points

### Document vs Code vs Operations

- **`docs/`**: Holds "Why" and "What" (PRD, ADR, ARD).
- **`docs/specs/`**: Holds "Exactly How" prior to coding.
- **`docs/plans/`**: Holds "When" and "Who" during execution.
- **`docs/runbooks/`**: Holds executable scripts and "What to do when X fails."

### Extending the Architecture

1. **Design Changes**: Create an ADR in `docs/adr/` using `templates/adr-template.md`.
2. **Data Structure Changes**: Document via ARD in `docs/ard/` using `templates/ard-template.md`.
3. **Execution Rules**: Modify `.agent/rules/` to enforce new architectural linters globally.

---

> **Note**: This architecture document must be kept strictly to high-level system design. For operational procedures, alerting logic, or CI orchestration, consult `OPERATIONS.md`.
