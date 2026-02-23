@echo off
echo ============================================
echo  Voice Clone Project - Starting Server
echo ============================================

cd /d "%~dp0.."

REM Activate the main virtual environment
call venv\Scripts\activate.bat

REM Start the FastAPI server from project root
echo Starting FastAPI server on http://localhost:8000 ...
python -m src.app

pause
