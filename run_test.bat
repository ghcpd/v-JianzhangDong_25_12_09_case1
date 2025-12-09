@echo off

REM Test runner script for Windows

echo Running tests...

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run tests
python -m pytest tests/ -v

echo Tests completed.

pause