@echo off
REM Create logs dir if missing
if not exist logs mkdir logs
set LOGFILE=logs\test_run.log
echo Running tests %date% %time%>> %LOGFILE%

IF EXIST .venv (
  echo Using .venv\Scripts\python to run tests>> %LOGFILE%
  set PYTHON=.venv\Scripts\python
) ELSE (
  echo Using system python to run tests>> %LOGFILE%
  set PYTHON=python
)
set PYTHONPATH=%CD%
for %%f in (tests\*.py) do (
  echo --- Running %%f --- >> %LOGFILE%
  %PYTHON% %%f >> %LOGFILE% 2>&1
)

echo Tests completed %date% %time%>> %LOGFILE%
