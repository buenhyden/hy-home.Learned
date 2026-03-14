# Runbook: Documentation Ecosystem Maintenance

- **Status**: Active
- **Owner**: buenhyden
- **Last Reviewed**: 2026-03-14
- **layer:** agentic

**Overview (KR):** 프로젝트 문서 체계와 AI Agent 지침을 최상의 상태로 유지하기 위한 정기 점검 및 관리 지침서입니다.

## Purpose

Maintaining documentation integrity is critical for AI agent performance. This runbook ensures that metadata is preserved and links remain functional as the project evolves.

## Review Checklist

- [ ] Every new MD file in `docs/` has a `layer:` tag.
- [ ] Every new MD file uses the correct template from `templates/`.
- [ ] Relative links between `adr`, `ard`, and `specs` are functional.
- [ ] Triggers in `.agent/rules/` correctly point to deep context in `docs/agentic/`.

## Procedure

1. Run link checker tool (if available).
2. Manually verify `layer:` metadata presence.
3. Update `docs/agentic/README.md` index if new standards are added.

## Related Operational Documents

- **Incident examples**: `[../operations/incidents/]`
- **Postmortem examples**: `[../operations/postmortems/]`
