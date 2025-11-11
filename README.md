# Colab - 온프레미스 Python 실행 환경

Django 기반의 안전한 Python 코드 실행 환경 제공 시스템

## 프로젝트 개요

온프레미스 환경에서 안전하게 Python 코드를 실행할 수 있는 개발 환경을 제공합니다.

### 주요 기능

- ✅ 안전한 Python 코드 실행 (RestrictedPython 기반)
- ✅ 템플릿 기반 개발 환경
- ✅ Framework DB 연결 지원
- ✅ 코드 파일 관리 (조회, 열기, 저장)
- ✅ JSON 기반 API 제공
- ✅ Docker 격리 실행 지원 (선택)

## 기술 스택

- **Backend**: Django 4.2+, Django REST Framework
- **Python 실행**: RestrictedPython
- **데이터 처리**: NumPy, Pandas, Scikit-learn, Matplotlib
- **보안**: Docker 격리 (선택)

## 설치 및 실행

### 1. 가상환경 생성 및 활성화

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정

`.env` 파일을 생성하고 필요한 설정을 추가합니다:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 4. 데이터베이스 마이그레이션

```bash
python manage.py migrate
```

### 5. 개발 서버 실행

```bash
python manage.py runserver
```

## 프로젝트 구조

```
colab/
├── docs/                 # 문서
│   └── ARCHITECTURE.md   # 아키텍처 설계 문서
├── colab/                # Django 프로젝트 설정
│   ├── settings/         # 설정 파일들
│   ├── urls.py          # 메인 URL 설정
│   └── wsgi.py          # WSGI 설정
├── apps/                 # Django 앱들
│   ├── core/            # 핵심 기능
│   ├── execution/       # 코드 실행 엔진
│   ├── templates/       # 템플릿 관리
│   ├── files/           # 파일 관리
│   └── api/             # API 엔드포인트
├── execution_engine/     # Python 실행 엔진
│   ├── restricted/      # RestrictedPython 실행기
│   └── docker/          # Docker 격리 실행기
├── templates/            # Python 템플릿 파일들
├── static/              # 정적 파일
├── media/               # 미디어 파일
├── requirements.txt     # Python 의존성
└── manage.py           # Django 관리 스크립트
```

## API 문서

API 엔드포인트는 `/api/v1/` 경로를 통해 제공됩니다.

- `POST /api/v1/execute/` - Python 코드 실행
- `GET /api/v1/templates/` - 템플릿 목록 조회
- `GET /api/v1/files/` - 파일 목록 조회
- `POST /api/v1/files/` - 파일 생성/저장

## 보안

- RestrictedPython을 통한 안전한 코드 실행
- 허용된 라이브러리만 사용 가능
- 위험한 함수 및 모듈 차단
- Docker 격리 실행 지원 (선택)

## 라이선스

내부 사용 전용

