# Next.JS Folder Structure

```
my-next-app/
│
├── .next/                     # 빌드 생성 디렉터리
│   ├── cache/
│   └── ...
│
├── api-lib/                   # API 호출과 관련된 로직 라이브러리
│   ├── userApi.js
│   └── postApi.js
│
├── assets/                    # 다양한 미디어 자원을 저장하는 디렉터리
│   ├── images/
│   └── icons/
│
├── docs/                      # 필요한 참고문서를 저장하는 디렉터리
│   ├── Frontend/
│   ├── Backend/
│   └── Design/
│
├── components/                # 재사용 가능한 UI 컴포넌트를 저장하는 디렉터리
│   ├── Header.js
│   ├── Footer.js
│   └── ...
│
├── hooks/                     # 커스텀훅을 저장하는 디렉터리
│   ├── useTimeFormat.js
│   └── ...
│
├── lib/                       # 외부 라이브러리 또는 프로젝트 내부에서 사용하는 유틸리티 함수
│   ├── util.js
│   └── helper.js
│
├── page-components/           # 특정 페이지에서만 사용되는 컴포넌트를 저장하는 디렉터리
│   ├── HomePageComponents/
│   └── AboutPageComponents/
│
├── pages/                     # 페이지 컴포넌트 및 API 라우트를 저장하는 디렉터리
│   ├── _app.js
│   ├── _document.js
│   ├── index.js
│   └── api/                   # API를 저장하는 디렉터리
│       └── user.js
│
├── styles/                    # scss, 스타일을 저장하는 디렉터리
│   ├── globals.scss
│   ├── Home.module.scss
│   └── ...
│
├── mocks/                     # 더미 객체를 저장하는 디렉터리 (api 연결 전에 테스트)
│   ├── handler.js
│   └── ...
│
├── public/                    # 정적 파일을 저장하는 디렉터리
│   ├── favicon.ico
│   └── logo.png
│
├── package.json               # 프로젝트의 의존성과 스크립트를 정의하는 파일
└── README.md                  # 프로젝트에 대한 정보 및 사용 방법을 설명하는 파일
```
