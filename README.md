# hy-home.Learned

이 저장소는 개인 학습 자산과 AI Agent 협업 규칙을 함께 관리하는 Python 기반 지식 저장소입니다. 학습 노트는 `TIL/`에, 실행 가능한 문서 체계는 `docs/`에, 자동화와 검증 기준은 `.github/`와 `.agent/`에 모아 둡니다.

## 현재 구조

- `TIL/`: 날짜 기반 학습 노트와 실험 기록
- `tests/`: 저장소 전역 테스트 자산과 테스트 전략 문서
- `docs/`: 요구사항, 설계, 계획, 운영 기록을 담는 숫자형 문서 체계
- `docs/00.agent-governance/`: AI Agent 전용 거버넌스 허브
- `.agent/`: 레거시 규칙 및 워크플로 호환 레이어
- `.github/workflows/ci.yml`: CI 진실 원천

## 문서 흐름

모든 변경은 다음 흐름을 기준으로 추적합니다.

`01.prd` -> `02.ard` / `03.adr` -> `04.specs` -> `05.plans` -> `06.tasks` -> `07~11`

의미:

- `01.prd`: 무엇을 왜 하는지
- `02.ard` / `03.adr`: 구조와 중요한 결정
- `04.specs`: 구현 계약과 검증 기준
- `05.plans`: 실행 순서와 리스크 관리
- `06.tasks`: 작업 단위와 증거
- `07~11`: 가이드, 운영, 런북, 사고, 회고

## AI Agent 거버넌스

리팩터링 이후 `docs/00.agent-governance/`는 `examples/00.agent-governance/`와 동일한 상위 구조를 따릅니다.

- `rules/`: 공통 규칙, persona, README 동기화, 품질 기준
- `scopes/`: 작업 레이어별 세부 규칙
- `providers/`: Claude / Gemini 전용 메모
- `memory/`: 선택적 메모리 템플릿

루트 entrypoint 역할은 다음과 같이 분리됩니다.

- `AGENTS.md`: 모든 에이전트가 읽는 공통 bootstrap
- `CLAUDE.md`: `AGENTS.md`와 Claude provider note를 import하는 thin shim
- `GEMINI.md`: `AGENTS.md`와 Gemini provider note를 import하는 thin shim

## 언어 정책

이 저장소는 문서 목적에 따라 언어를 분리합니다.

- 사람 중심 문서: 한국어
  - 루트 `README.md`
  - 저장소 개요성 안내 문서
- AI Agent 실행 문서: 영어
  - `docs/00.agent-governance/`
  - AI Agent가 직접 읽는 새 PRD / Spec / 운영 규칙

즉, 사람을 위한 안내는 한국어로 유지하고, 에이전트가 직접 로드하는 운영 지침은 영어로 유지합니다.

## 현재 실행 환경

- Python: `>=3.13`
- Package manager / runner: `uv`
- 주요 소스 영역: `TIL/`
- 테스트 진입점: `tests/`
- CI 기준: `.github/workflows/ci.yml`

대표 명령:

```bash
uv sync --all-extras --dev
uv run pre-commit run --all-files --hook-stage commit
uv run pre-commit run --all-files --hook-stage pre-push
```

## `.agent` 레이어에 대해

`.agent/`는 현재 완전히 제거하지 않고 호환성 레이어로 유지합니다. 다만 primary governance source는 아니며, 최신 기준은 항상 다음 순서를 따릅니다.

1. 루트 `AGENTS.md`
2. `docs/README.md`
3. `docs/00.agent-governance/`

## 시작 순서

사람과 에이전트 모두 다음 순서로 진입하면 됩니다.

1. 이 `README.md`
2. [docs/README.md](./docs/README.md)
3. [AGENTS.md](./AGENTS.md)
4. 필요 시 `docs/00.agent-governance/` 아래 세부 문서
