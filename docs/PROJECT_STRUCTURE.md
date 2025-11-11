# 프로젝트 구조

## 디렉토리 구조

```
colab/
├── docs/                          # 문서
│   ├── ARCHITECTURE.md           # 아키텍처 설계 문서
│   ├── API.md                    # API 문서
│   └── PROJECT_STRUCTURE.md      # 프로젝트 구조 문서
│
├── colab/                        # Django 프로젝트 설정
│   ├── settings/                 # 설정 파일들
│   │   ├── __init__.py
│   │   ├── base.py              # 기본 설정
│   │   ├── development.py       # 개발 환경 설정
│   │   └── production.py        # 프로덕션 환경 설정
│   ├── __init__.py
│   ├── urls.py                  # 메인 URL 설정
│   ├── wsgi.py                  # WSGI 설정
│   └── asgi.py                  # ASGI 설정
│
├── apps/                         # Django 앱들
│   ├── core/                    # 핵심 기능
│   │   ├── models.py            # 공통 모델 (BaseModel)
│   │   └── apps.py
│   │
│   ├── execution/               # 코드 실행
│   │   ├── models.py            # ExecutionLog, ExecutionResult
│   │   ├── services.py          # 실행 서비스 로직 (추후 구현)
│   │   ├── views.py             # API 뷰 (추후 구현)
│   │   └── urls.py              # URL 라우팅 (추후 구현)
│   │
│   ├── templates/               # 템플릿 관리
│   │   ├── models.py            # Template, TemplateCategory
│   │   ├── services.py          # 템플릿 서비스 로직 (추후 구현)
│   │   ├── views.py             # API 뷰 (추후 구현)
│   │   └── urls.py              # URL 라우팅 (추후 구현)
│   │
│   ├── files/                   # 파일 관리
│   │   ├── models.py            # CodeFile
│   │   ├── services.py          # 파일 서비스 로직 (추후 구현)
│   │   ├── views.py             # API 뷰 (추후 구현)
│   │   └── urls.py              # URL 라우팅 (추후 구현)
│   │
│   └── api/                     # API 엔드포인트 통합
│       └── urls.py              # API URL 통합
│
├── execution_engine/             # Python 실행 엔진
│   ├── base.py                  # ExecutionEngine 기본 클래스
│   ├── factory.py               # 실행 엔진 팩토리
│   └── restricted/              # RestrictedPython 실행기
│       ├── __init__.py
│       └── engine.py            # RestrictedPythonEngine
│
├── templates/                    # Python 템플릿 파일들 (추후 추가)
│   ├── grid/                    # 그리드 조회 템플릿
│   ├── chart/                   # 차트 템플릿
│   ├── regression/              # 회귀분석 템플릿
│   └── classification/          # 분류분석 템플릿
│
├── static/                       # 정적 파일
├── media/                        # 미디어 파일
│   └── code_files/              # 사용자 코드 파일 저장소
│
├── logs/                         # 로그 파일 (자동 생성)
│
├── manage.py                     # Django 관리 스크립트
├── requirements.txt              # Python 의존성
├── README.md                     # 프로젝트 README
└── .gitignore                    # Git 무시 파일
```

## 주요 컴포넌트

### 1. Django 설정 (colab/settings/)

- **base.py**: 모든 환경에서 공통으로 사용하는 기본 설정
- **development.py**: 개발 환경 설정 (DEBUG=True 등)
- **production.py**: 프로덕션 환경 설정 (보안 강화)

### 2. Django 앱

#### apps/core
- 공통 모델 및 유틸리티
- `BaseModel`: 생성일시, 수정일시, 생성자, 수정자 필드를 가진 추상 모델

#### apps/execution
- 코드 실행 관련 기능
- `ExecutionLog`: 코드 실행 로그 저장
- `ExecutionResult`: 실행 결과 캐싱

#### apps/templates
- Python 코드 템플릿 관리
- `Template`: 템플릿 정보 및 코드 저장
- `TemplateCategory`: 템플릿 카테고리 분류

#### apps/files
- 사용자 코드 파일 관리
- `CodeFile`: 사용자별 코드 파일 저장 및 관리

### 3. 실행 엔진 (execution_engine/)

#### execution_engine/base.py
- `ExecutionEngine`: 모든 실행 엔진의 기본 인터페이스
- `execute()`: 코드 실행 메서드
- `validate_code()`: 코드 유효성 검사 메서드

#### execution_engine/restricted/
- `RestrictedPythonEngine`: RestrictedPython 기반 실행 엔진
- 안전한 코드 실행 환경 제공
- 허용된 모듈만 import 가능
- 위험한 함수 차단

#### execution_engine/factory.py
- `ExecutionEngineFactory`: 실행 모드에 따라 적절한 엔진 생성

## 데이터 모델 관계

```
User
 ├── ExecutionLog (코드 실행 로그)
 ├── CodeFile (코드 파일)
 └── Template (생성한 템플릿)

TemplateCategory
 └── Template (템플릿)

ExecutionResult (실행 결과 캐시)
```

## 보안 계층

1. **코드 검증**: RestrictedPython을 통한 문법 및 위험 함수 검사
2. **모듈 제한**: 화이트리스트 기반 허용 모듈만 import 가능
3. **실행 격리**: RestrictedPython 또는 Docker를 통한 격리 실행
4. **리소스 제한**: 타임아웃, 메모리 제한 설정

## 다음 단계

1. API 뷰 및 시리얼라이저 구현
2. 템플릿 파일 추가
3. Framework DB 연결 모듈 구현
4. Docker 실행 엔진 구현 (선택)
5. 프론트엔드 UI 개발

