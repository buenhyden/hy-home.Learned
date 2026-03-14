# Responsible AI Standards

> **layer:** agentic
> **Status**: Active Detail Layer
> **Source**: Refactored from `.agent/rules/0100-Standards/0106-responsible-ai.md`

## 1. Principles

- **Fairness**: AI MUST not discriminate based on protected characteristics.
- **Transparency**: Users MUST know they are interacting with AI.
- **Privacy**: User PII MUST be protected (sanitized) before AI processing.

## 2. Must / Must Not

- **Accessibility**: AI Interfaces MUST meet WCAG 2.1 AA (Keyboard, Screen Reader).
- **No Secrets**: API Keys/Secrets MUST NOT be sent to LLMs.
- **Bias Testing**: Models MUST be tested against diverse inputs.

## 3. Data Sanitization Procedure

1. **Identify**: Email, Phone, SSN, Credit Card.
2. **Action**: Replace with placeholders (`<EMAIL>`) or Redact.
3. **Log**: Record that redaction occurred.

## 4. Validation Criteria

- [ ] UI passes automated accessibility scan (axe-core).
- [ ] No PII detected in prompt logs.
- [ ] UI clearly labels content as "AI Generated".
