# Node.js Express Folder Structure

```
my-express-app/
│
├── routes/                 # 라우터 파일들을 저장합니다.
│   ├── index.js            # 기본 라우트를 정의합니다.
│   └── users.js            # 사용자 관련 라우트를 정의합니다.
│
├── controllers/            # 컨트롤러를 저장합니다.
│   ├── indexController.js  # 'index' 경로의 컨트롤러입니다.
│   └── userController.js   # 'user' 경로의 컨트롤러입니다.
│
├── services/               # 서비스 로직을 저장합니다.
│   └── userService.js      # 사용자 관련 서비스 로직입니다.
│
├── models/                 # 데이터 모델 파일들을 저장합니다.
│
├── utils/                  # 유틸리티 함수를 저장합니다.
│   └── helpers.js          # 다양한 유틸리티 함수를 포함합니다.
│
├── middleware/             # 미들웨어 파일들을 저장합니다.
│
├── tests/                  # 테스트 코드를 저장합니다.
│   ├── unit/               # 유닛 테스트 코드를 저장합니다.
│   └── integration/        # 통합 테스트 코드를 저장합니다.
│
├── docs/                   # 문서화 관련 파일들을 저장합니다.
│   ├── api/                # API 문서를 저장합니다.
│   └── setup.md            # 개발 환경 설정 문서입니다.
│
├── app.js                  # 앱 설정과 미들웨어를 정의합니다.
│
├── package.json            # 프로젝트의 의존성과 스크립트를 정의합니다.
│
└── README.md               # 프로젝트에 대한 설명을 담은 README 파일입니다.
```
