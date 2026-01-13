# Learned: Professional Knowledge Archive

개인적인 학습 여정, 기술적 연구, 그리고 AI 기반의 지식 관리를 위한 중앙 저장소입니다.
(Central repository for personal learning journeys, technical research, and AI-driven knowledge management.)

---

## 🚀 Key Features

- **AI-First Workflow**: 45개 이상의 전용 에이전트와 지침을 활용한 지능형 개발 및 학습 환경.
- **Structured Learning**: `Studies`, `TIL`, `References`로 구분된 체계적인 지식 아카이브.
- **Modern Infrastructure**: 테스트와 실험을 위한 Docker 및 클라우드 네이티브 설정 포함.

## 📂 Repository Structure

| Folder | Description |
| :--- | :--- |
| **[TIL/](./TIL)** | **Today I Learned**. 2024~2026년의 일일 학습 및 문제 해결 기록. |
| **[References/](./References)** | **Knowledge Base**. 도서(Books), 강의 자료(Lecture-Data) 등 학습 리소스 아카이브. |
| **[.agent/](./.agent)** | **AI Configuration**. Agentic Workflow 규칙 및 설정. |
| **[.github/](./.github)** | **Project Management**. 템플릿, 워크플로우, 커뮤니티 건강 파일(Community Health Files). |

### 📚 Key Documents

| File | Description |
| :--- | :--- |
| **[AGENTS.md](./AGENTS.md)** | 사용 가능한 45+ AI 에이전트 목록 및 설명. |
| **[GEMINI.md](./GEMINI.md)** | Antigravity(Gemini) 모델의 역할 및 가이드. |
| **[CLAUDE.md](./CLAUDE.md)** | Claude 모델의 역할 및 가이드. |

## 🤖 AI Orchestration

이 저장소는 AI 도구(Cursor, Claude, Gemini)와의 협업을 최적화하도록 설계되었습니다.

- **[Specialized Agents](./AGENTS.md)**: 45개 이상의 특화된 에이전트 페르소나 안내.
- **[Gemini Guide](./GEMINI.md)**: Antigravity(Gemini) 모델의 역할 및 상호작용 방식.
- **[Claude Guide](./CLAUDE.md)**: Claude의 역할 및 주요 워크플로우 안내.
- **[.cursorrules](./.cursorrules)**: AI 에디터(Cursor 등)를 위한 컨텍스트 규칙.

## 🛠️ Usage & Setup

### ⚡ Getting Started

이 프로젝트는 **`uv`** 를 사용하여 의존성을 관리합니다.

1. **Prerequisites**: Python 3.13+, Docker, [uv](https://github.com/astral-sh/uv).
2. **Setup**:

    ```bash
    # 의존성 설치 (Sync dependencies)
    uv sync
    ```

3. **AI Tools**: 프로젝트 루트의 `.cursorrules`와 `.github/instructions/`가 AI 도구에 의해 자동으로 인식됩니다.
4. **Contribution**: 학습 및 연구 기록 시 [CONTRIBUTING.md](./.github/CONTRIBUTING.md)의 AI 정책을 준수하십시오.

## 📄 License & Contact

- **License**: [MIT License](./LICENSE)
- **Author**: buenhyden ([chochyjj@gmail.com](mailto:chochyjj@gmail.com))
- **Links**: [GitHub Discussions](https://github.com/buenhyden/hy-home.Learned/discussions)

---

## Troubleshooting

### 1. `pre-commit run --all-files` 실행 시 `pyproject.toml` 파일 인코딩 오류

이 에러는 윈도우(Windows) 환경에서 파이썬(Python)이 `pyproject.toml` 파일을 읽을 때, 시스템 기본 인코딩인 **CP949**를 사용하여 **UTF-8**로 작성된 문자를 해석하려다 발생한 전형적인 **인코딩 충돌(Encoding Mismatch)** 문제.

`pyproject.toml` 표준 스펙은 반드시 **UTF-8** 인코딩을 사용해야 하지만, 일부 윈도우 환경의 도구들이 이를 무시하고 시스템 설정을 따르기 때문에 발생한다.

#### 해결책

1. 파이썬 UTF-8 모드 강제 활성화:
    파이썬 3.7 이상부터 지원하는 **UTF-8 모드**를 활성화하면, 시스템 설정과 상관없이 모든 입출력을 UTF-8로 처리한다. 터미널(PowerShell 또는 CMD)에서 아래 명령어를 입력하여 환경 변수를 설정.
    1. PowerShell (현재 세션 적용)

        ```powershell
        $env:PYTHONUTF8 = "1"
        # 이후 다시 실행
        pre-commit run --all-files

        ```

    2. 시스템 환경 변수 설정 (영구 적용)
        1. `윈도우 키 + R` -> `sysdm.cpl` 입력 -> [확인]
        2. [고급] 탭 -> [환경 변수] 클릭
        3. [시스템 변수] 섹션에서 [새로 만들기] 클릭
        4. 변수 이름: `PYTHONUTF8`, 변수 값: `1` 입력 후 확인

2. `pyproject.toml` 파일 인코딩 확인
    파일 내부에 한글 주석이나 특수 문자가 포함되어 있을 경우, 실제 파일 저장 형식이 UTF-8이 아닐 수 있다.
    1. **VS Code** 사용 시: 우측 하단 상태 표시줄의 인코딩이 `UTF-8`인지 확인한다. 만약 `CP949`나 `EUC-KR`로 되어 있다면 클릭하여 `Save with Encoding` -> `UTF-8`을 선택한다.
    2. **BOM 제거:** UTF-8(with BOM) 형식이 아닌 **UTF-8(without BOM)** 형식을 사용해야 한다.

3. 해결 방법 3: pre-commit hook 설정 보완
    만약 특정 훅(hook)에서만 문제가 발생한다면, `PYTHONUTF8=1` 환경 변수를 훅 실행 시점에 직접 전달하도록 시도할 수 있다. 하지만 일반적으로 **방법 1**이 가장 권장된다.

    ```yaml
    # .pre-commit-config.yaml 예시
    - repo: https://github.com/abravalheri/validate-pyproject
    rev: v0.15
    hooks:
        - id: validate-pyproject
        # 특정 환경에서만 문제가 된다면 훅 설정을 점검할 수 있으나,
        # 근본적인 해결은 환경 변수 설정입니다.

    ```

**참고 문헌 (References):**

- [Python 3.7+ UTF-8 Mode (PEP 540)](https://peps.python.org/pep-0540/)
- [pyproject.toml Specification (PEP 518)](https://peps.python.org/pep-0518/)

---
