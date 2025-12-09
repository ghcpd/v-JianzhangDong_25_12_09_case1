@echo off
if not exist .venv\Scripts\python.exe (
  echo .venv not found. Run setup.sh or setup in Windows.
  exit /b 1
)
set PYTHONPATH=%CD%
.venv\Scripts\python.exe -u -c "import sys; print('Python', sys.version)"
for %%f in (tests\*.py) do (
  echo ----- Running %%f -----
  .venv\Scripts\python.exe "%%f"
)
echo Done.
