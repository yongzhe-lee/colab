@echo off
REM JupyterHub 시작 스크립트 (Windows)
cd /d %~dp0\..

REM 가상환경 활성화 (있는 경우)
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

REM JupyterHub 시작
python scripts\start_jupyterhub.py

pause



