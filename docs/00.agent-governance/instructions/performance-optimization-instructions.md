# Performance Optimization Instructions

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0000-Agents/0016-performance-optimization-standard.md`

## 1. Principles

- **Mandatory Measurement-First Protocol**: No optimization without a baseline.
- **80/20 Impact Prioritization**: Focus on 20% of code causing 80% latency.
- **Strict Performance Budgeting**: LCP < 2.5s, API Response < 200ms.

## 2. Optimization Matrix

- **Measurement**: `EXPLAIN ANALYZE`, Lighthouse, or Profilers.
- **Caching**: Layered caching with explicit TTL strategies.
- **Backend**: Avoid N+1 queries; use batch operations.
- **Frontend**: Tree-shaking and asset compression.

## 3. Mandatory Requirements

- **Verifiable Before/After Proof**: Report showing quantified delta.
- **Explicit Hot-Path Identification**: Document bottleneck before implementation.
- **Preservation of Functional Logic**: unit tests MUST pass after modification.

## 4. Procedures

1. **Capture Baseline**
2. **Profiling (Hot Path)**
3. **Strategy Selection**
4. **Implementation**
5. **Final Verification (Proof)**

## 5. Validation Criteria

- [ ] Baseline measurement captured and documented.
- [ ] Optimization resulted in > 10% improvement or met budget.
- [ ] 100% of functional tests pass after modification.
