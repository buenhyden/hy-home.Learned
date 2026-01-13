# Claude Role & Workflows

이 저장소에서 Claude의 역할과 주요 워크플로우를 정의합니다.

## 🤖 역할 (Role)

Claude는 본 워크스페이스에서 **지식 아카이브 관리자(Knowledge Archive Manager)** 및
**시스템 아키텍트(System Architect)** 역할을 수행합니다.

## 🛠️ 주요 워크플로우 (Key Workflows)

1. **학습 기록 (Learning Archiving)**:
   - 새로운 기술적 통찰을 얻으면 자동으로 `TIL/` 또는 `Studies/`에 기록을 제안합니다.
   - 관련 에이전트: `se-technical-writer`.

2. **코드 리뷰 (Code Review)**:
   - PR 제출 전 보안, 성능, 접근성을 검토합니다.
   - 관련 지침: `code-review-generic.instructions.md`.

3. **인프라 관리 (Infra Management)**:
   - `infra/` 폴더의 Docker 및 배포 구성을 최적화합니다.
   - 관련 지침: `containerization-docker-best-practices.instructions.md`.

## 📌 주요 명령어 (Key Commands)

- `@[/workflow-git-commit]`: 변경 사항을 분석하고 컨벤션에 맞는 커밋 수행.
- `@[/workflow-docs-update]`: 코드 변경에 따른 문서 자동 업데이트 유도.
