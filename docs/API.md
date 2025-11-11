# API 문서

## 기본 정보

- Base URL: `/api/v1/`
- 인증: Session Authentication (기본)
- 응답 형식: JSON

## 엔드포인트

### 1. 코드 실행

#### POST /api/v1/execute/

Python 코드를 실행하고 결과를 반환합니다.

**Request Body:**
```json
{
    "code": "print('Hello World')",
    "execution_mode": "restricted",
    "timeout": 30
}
```

**Response (Success):**
```json
{
    "status": "success",
    "output": "Hello World\n",
    "error": null,
    "execution_time": 0.123,
    "memory_used": 0
}
```

**Response (Error):**
```json
{
    "status": "error",
    "output": "",
    "error": "허용되지 않은 함수 'open'이 사용되었습니다.",
    "execution_time": 0.001,
    "memory_used": 0
}
```

### 2. 템플릿 관리

#### GET /api/v1/templates/

템플릿 목록을 조회합니다.

**Query Parameters:**
- `category`: 카테고리 필터
- `search`: 검색어

**Response:**
```json
{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "그리드 조회",
            "category": "grid",
            "description": "데이터 그리드 조회 템플릿",
            "code": "...",
            "is_active": true,
            "is_public": true
        }
    ]
}
```

#### GET /api/v1/templates/{id}/

특정 템플릿을 조회합니다.

#### POST /api/v1/templates/

새 템플릿을 생성합니다.

### 3. 파일 관리

#### GET /api/v1/files/

사용자의 코드 파일 목록을 조회합니다.

**Response:**
```json
{
    "count": 5,
    "results": [
        {
            "id": 1,
            "name": "example.py",
            "code": "print('Hello')",
            "file_type": "py",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        }
    ]
}
```

#### POST /api/v1/files/

새 코드 파일을 생성합니다.

#### GET /api/v1/files/{id}/

특정 파일을 조회합니다.

#### PUT /api/v1/files/{id}/

파일을 수정합니다.

#### DELETE /api/v1/files/{id}/

파일을 삭제합니다.

### 4. 실행 로그

#### GET /api/v1/execution-logs/

실행 로그 목록을 조회합니다.

#### GET /api/v1/execution-logs/{id}/

특정 실행 로그를 조회합니다.

