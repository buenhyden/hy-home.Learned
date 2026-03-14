# MCP Developer Instructions

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0000-Agents/0003-mcp-developer-standard.md`

## 1. Principles

- **Protocol-First Fidelity**: Adhere strictly to official MCP specification.
- **Immutable Type Safety**: Strict schemas (Zod/Pydantic) for all inputs/outputs.
- **Mandatory Protocol Observability**: Structured logging of protocol events to `stderr`.

## 2. Integration Baseline

- **Schema**: Zod / Pydantic (No `any`).
- **Transport**: Stdio (CLI/Local) or SSE (Remote/Web).
- **Lifecycle**: Explicit `connect` and `shutdown` handling.
- **Error**: Standard JSON-RPC error codes.

## 3. Mandatory Requirements

- **Verified Inspector Boot**: Successful verification using official MCP Inspector.
- **Explicit Capability Declaration**: Declare Tools/Resources/Prompts support.
- **Non-Blocking Handlers**: implementation as asynchronous functions.

## 4. Procedures

- **Protocol Verification Cycle**: Run `npx @modelcontextprotocol/inspector <command>` after tool modifications.
- **Transport Hardening**: Verify connection timeout and reconnection handling for SSE.

## 5. Validation Criteria

- [ ] Server initializes and lists features in Inspector without errors.
- [ ] 100% of tools utilize strict, typed schemas.
- [ ] Zero non-protocol data emitted to `stdout`.
