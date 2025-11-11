"""
Django 인증과 연동하는 JupyterHub Authenticator
"""
import os
import sys
from pathlib import Path

# Django 설정 로드
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'colab.settings.development')

import django
django.setup()

from jupyterhub.auth import Authenticator
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class DjangoAuthenticator(Authenticator):
    """
    Django 인증 시스템과 연동하는 JupyterHub Authenticator
    """
    
    async def authenticate(self, handler, data):
        """
        Django 사용자 인증 처리
        
        Args:
            handler: Tornado request handler
            data: 폼 데이터 (username, password 포함)
            
        Returns:
            username 또는 None
        """
        username = data.get('username', '')
        password = data.get('password', '')
        
        if not username or not password:
            return None
        
        # Django 인증 시스템을 사용하여 사용자 인증
        user = authenticate(username=username, password=password)
        
        if user and user.is_active:
            return username
        return None
    
    async def pre_spawn_start(self, user, spawner):
        """
        사용자 서버 시작 전 실행
        """
        # Django 사용자 정보를 spawner 환경 변수로 전달
        try:
            django_user = User.objects.get(username=user.name)
            spawner.environment['DJANGO_USER_ID'] = str(django_user.id)
            spawner.environment['DJANGO_USERNAME'] = django_user.username
            spawner.environment['DJANGO_EMAIL'] = django_user.email or ''
        except User.DoesNotExist:
            pass



