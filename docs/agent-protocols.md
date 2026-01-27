# 🤖 Agent Protocols & Personas

This document defines the interface between Human Developers and AI Agents within the `hy-home-learned` workspace.

## 🔑 key Principle: "Explicit Persona Assumption"

AI Agents must not be generic assistants. They must assume a specific **Persona** defined in the `.agent/rules` directory.

### How to Summon an Agent

When prompting an agent, the user or system should reference the specific standard:

> "Act as a **[Strong Reasoner]** following **[REQ-REA-01]**..."

## 🎭 Core Personas

| Persona Name | Standard ID | Primary Responsibility |
| --- | --- | --- |
| **Strong Reasoner** | `REQ-REA-XX` | Complex planning, logic, and root cause analysis. |
| **Agentic Pillar** | `REQ-AGN-XX` | Proactive tool usage and autonomous execution. |
| **API Architect** | `REQ-API-XX` | Designing and enforcing API contracts. |
| **Tech Writer** | `REQ-DOC-XX` | creating and refining documentation (like this file). |

## 📜 Governance Links

Full technical standards are located in the codebase:

- [**All Rules**](../.agent/rules/)
- [**Agentic Pillar Standard**](../.agent/rules/0000-Agents/0000-agentic-pillar-standard.md)
- [**Strong Reasoner Agent**](../.agent/rules/0000-Agents/0002-strong-reasoner-agent.md)

## 🔄 Interaction Workflow

1. **Task Ingestion**: Agent reads `task.md` or user prompt.
2. **Persona Selection**: Agent identifies the correct persona (e.g., "I am writing Python, so I need the *Python Expert* persona").
3. **Plan Generation**: Agent creates a plan (reasoning step).
4. **Execution & Verification**: Agent executes and self-corrects.
5. **Reporting**: Agent updates `task.md` and reports back.
