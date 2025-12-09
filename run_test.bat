@echo off
REM run_test.bat - Test execution script for Windows

echo.
echo ==========================================
echo Running tests on Windows
echo ==========================================

REM Check if .venv exists
if not exist ".venv" (
    echo Error: Virtual environment not found at .venv
    echo Please run the environment setup first
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Display environment info
echo.
python --version
pip --version
echo.

REM Create logs directory if it doesn't exist
if not exist "logs" (
    mkdir logs
)

REM Run auto_test.py
echo Executing auto_test.py...
python auto_test.py

echo.
echo ==========================================
echo Tests completed. Check logs\test_run.log
echo ==========================================
pause
