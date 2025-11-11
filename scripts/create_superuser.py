"""
Django 슈퍼관리자 계정 생성 스크립트
"""
import os
import sys
import django

# Django 설정 로드
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'colab.settings.development')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    """슈퍼관리자 계정 생성"""
    username = 'admin'
    email = 'admin@colab.local'
    password = 'admin123'  # 기본 비밀번호 (변경 권장)
    
    # 이미 존재하는지 확인
    if User.objects.filter(username=username).exists():
        print(f"[INFO] 사용자 '{username}'가 이미 존재합니다.")
        user = User.objects.get(username=username)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        print(f"[SUCCESS] 사용자 '{username}'의 슈퍼관리자 권한이 업데이트되었습니다.")
    else:
        # 새 슈퍼관리자 생성
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"[SUCCESS] 슈퍼관리자 계정이 생성되었습니다!")
        print(f"   - 사용자명: {username}")
        print(f"   - 이메일: {email}")
        print(f"   - 비밀번호: {password}")
        print(f"\n[WARNING] 보안을 위해 비밀번호를 변경하세요!")

if __name__ == '__main__':
    create_superuser()

