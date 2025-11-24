# React Folder Structure

```
my-app/
│
├── public/                # 정적 파일들을 저장합니다.
│   ├── index.html         # 메인 HTML 파일입니다.
│   └── favicon.ico        # 웹사이트의 파비콘 아이콘입니다.
│
├── src/                   # 소스 코드를 저장하는 디렉터리입니다.
│   ├── components/        # 재사용 가능한 UI 컴포넌트들을 저장합니다.
│   │   ├── Layout/        # 레이아웃과 관련된 컴포넌트들입니다.
│   │   ├── Button/        # 버튼과 관련된 컴포넌트들입니다.
│   │   ├── Form/          # 폼과 관련된 컴포넌트들입니다.
│   │   ├── ListItem/      # 리스트 아이템과 관련된 컴포넌트들입니다.
│   │   └── Popup/         # 팝업과 관련된 컴포넌트들입니다.
│   │
│   ├── pages/             # 페이지 컴포넌트들을 저장합니다.
│   │
│   ├── services/          # API 호출이나 외부 서비스 로직을 저장합니다.
│   │
│   ├── contexts/          # React context를 사용한 전역 상태 관리 로직을 저장합니다.
│   │
│   ├── assets/            # 이미지, 폰트 등의 정적 리소스를 저장합니다.
│   │
│   ├── styles/            # SCSS 스타일 파일들을 저장합니다.
│   │
│   ├── utils/             # 유틸리티 함수를 저장합니다.
│   │
│   │
│   ├── mocks/             # 가짜 API 응답이나 테스트 데이터를 저장합니다.
│   │   └── users.js       # 사용자 데이터의 목업입니다.
│   │
│   ├── tests/             # 테스트 코드를 저장합니다.
│   │
│   ├── index.js           # 애플리케이션의 엔트리 포인트입니다.
│   └── App.js             # 메인 App 컴포넌트입니다.
│
├── .storybook/             # Storybook 설정 파일을 저장하는 디렉터리입니다.
│   ├── main.js             # Storybook의 기본 설정 파일입니다.
│   └── preview.js          # 컴포넌트 미리보기를 커스터마이징하는 파일입니다.
│
├── stories/                # Storybook 스토리 파일을 저장하는 디렉터리입니다.
│   ├── Button.stories.js   # Button 컴포넌트의 스토리 파일입니다.
│   └── ...
│
├── package.json           # 프로젝트의 의존성과 스크립트를 정의합니다.
├── README.md              # 프로젝트에 대한 설명을 담은 README 파일입니다.
└── ...
```
