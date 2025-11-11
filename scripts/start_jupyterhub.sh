#!/bin/bash
# JupyterHub 시작 스크립트 (Linux/Mac)

# 스크립트 디렉토리로 이동
cd "$(dirname "$0")/.."

# 가상환경 활성화 (있는 경우)
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

# JupyterHub 시작
python scripts/start_jupyterhub.py



