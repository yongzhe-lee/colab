"""
JupyterHub 설정 파일
Django 프로젝트와 통합된 JupyterHub 설정
"""
import os
import sys
from pathlib import Path

# 프로젝트 루트 디렉토리
BASE_DIR = Path(__file__).resolve().parent

# Django 설정 로드
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'colab.settings.development')

import django
django.setup()

from apps.jupyterhub.authenticator import DjangoAuthenticator

# JupyterHub 설정
c = get_config()  # noqa: F821

# =============================================================================
# JupyterHub 기본 설정
# =============================================================================

# JupyterHub가 실행될 IP와 포트
c.JupyterHub.ip = os.environ.get('JUPYTERHUB_IP', '127.0.0.1')
c.JupyterHub.port = int(os.environ.get('JUPYTERHUB_PORT', 8000))

# JupyterHub URL
c.JupyterHub.base_url = os.environ.get('JUPYTERHUB_BASE_URL', '/hub/')

# 쿠키 비밀키 (Django SECRET_KEY와 동일하게 설정 권장)
c.JupyterHub.cookie_secret_file = str(BASE_DIR / 'jupyterhub_cookie_secret')

# 데이터베이스 URL (SQLite 사용)
c.JupyterHub.db_url = f'sqlite:///{BASE_DIR / "jupyterhub.sqlite"}'

# =============================================================================
# 인증 설정
# =============================================================================

# Django 인증 시스템 사용
c.JupyterHub.authenticator_class = DjangoAuthenticator

# 로그인 페이지 설정
c.Authenticator.admin_users = {'admin'}  # 관리자 사용자 목록
c.Authenticator.auto_login = False

# =============================================================================
# Spawner 설정
# =============================================================================

# LocalProcessSpawner 사용 (로컬 프로세스로 실행)
c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'

# 사용자별 홈 디렉토리
c.LocalProcessSpawner.notebook_dir = str(BASE_DIR / 'notebooks' / '{username}')

# 사용자 서버 환경 변수
c.Spawner.env_keep = [
    'PATH',
    'PYTHONPATH',
    'CONDA_ROOT',
    'CONDA_DEFAULT_ENV',
    'VIRTUAL_ENV',
    'LANG',
    'LC_ALL',
    'DJANGO_SETTINGS_MODULE',
]

# 사용자 서버 시작 명령어
c.Spawner.cmd = ['jupyter-labhub']  # JupyterLab 사용

# 사용자 서버 타임아웃 (초)
c.Spawner.start_timeout = 60

# 사용자 서버 종료 타임아웃 (초)
c.Spawner.http_timeout = 30

# =============================================================================
# 서비스 설정
# =============================================================================

# 서비스 목록 (필요시 추가)
c.JupyterHub.services = []

# =============================================================================
# 보안 설정
# =============================================================================

# HTTPS 사용 여부 (프로덕션 환경에서 True로 설정)
c.JupyterHub.ssl_key = os.environ.get('JUPYTERHUB_SSL_KEY', '')
c.JupyterHub.ssl_cert = os.environ.get('JUPYTERHUB_SSL_CERT', '')

# CORS 설정
c.JupyterHub.tornado_settings = {
    'headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    }
}

# =============================================================================
# 로깅 설정
# =============================================================================

c.JupyterHub.log_level = os.environ.get('JUPYTERHUB_LOG_LEVEL', 'INFO')
c.JupyterHub.log_file = str(BASE_DIR / 'logs' / 'jupyterhub.log')

# =============================================================================
# 리소스 제한 설정
# =============================================================================

# CPU 제한 (사용자당)
c.Spawner.cpu_limit = float(os.environ.get('JUPYTERHUB_CPU_LIMIT', '2.0'))

# 메모리 제한 (사용자당, GB)
c.Spawner.mem_limit = os.environ.get('JUPYTERHUB_MEM_LIMIT', '2G')

# =============================================================================
# 사용자 디렉토리 생성
# =============================================================================

# 사용자 디렉토리 자동 생성
notebooks_dir = BASE_DIR / 'notebooks'
notebooks_dir.mkdir(exist_ok=True)



