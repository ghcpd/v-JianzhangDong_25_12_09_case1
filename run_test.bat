@echo off
IF NOT EXIST ".venv\Scripts\python.exe" (
  echo .venv does not exist. Run setup.sh or create the virtual environment first.
  exit /b 1
)
.venv\Scripts\python.exe auto_test.py
