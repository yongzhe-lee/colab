"""
JupyterHub 시작 스크립트
"""
import os
import sys
import subprocess
from pathlib import Path

# 프로젝트 루트 디렉토리
BASE_DIR = Path(__file__).resolve().parent.parent

def start_jupyterhub():
    """JupyterHub 시작"""
    # JupyterHub 설정 파일 경로
    config_file = BASE_DIR / 'jupyterhub_config.py'
    
    if not config_file.exists():
        print(f"[ERROR] JupyterHub 설정 파일을 찾을 수 없습니다: {config_file}")
        sys.exit(1)
    
    # JupyterHub 실행 명령어
    cmd = [
        sys.executable, '-m', 'jupyterhub',
        '--config', str(config_file),
        '--debug' if os.environ.get('DEBUG', 'False').lower() == 'true' else ''
    ]
    
    # 빈 문자열 제거
    cmd = [c for c in cmd if c]
    
    print(f"[INFO] JupyterHub 시작 중...")
    print(f"[INFO] 설정 파일: {config_file}")
    print(f"[INFO] 명령어: {' '.join(cmd)}")
    print(f"[INFO] JupyterHub는 http://127.0.0.1:8000/hub/ 에서 접근 가능합니다.")
    print(f"[INFO] 종료하려면 Ctrl+C를 누르세요.\n")
    
    try:
        # JupyterHub 실행
        subprocess.run(cmd, cwd=str(BASE_DIR))
    except KeyboardInterrupt:
        print("\n[INFO] JupyterHub 종료 중...")
    except Exception as e:
        print(f"[ERROR] JupyterHub 실행 중 오류 발생: {e}")
        sys.exit(1)

if __name__ == '__main__':
    start_jupyterhub()



