@echo off
echo ============================================
echo  Voice Clone Project - Starting Server
echo ============================================

cd /d "%~dp0.."

REM Activate the main virtual environment
call venv\Scripts\activate.bat

REM Start the FastAPI server via uvicorn from project root
echo.
echo Starting FastAPI server on http://localhost:8000 ...
echo Press Ctrl+C to stop.
echo.
python -m uvicorn src.app:app --host 0.0.0.0 --port 8000 --workers 1

pause
