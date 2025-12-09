# Environment and Test Automation

This project contains generated files to reproduce a clean Python environment, run tests, and collect logs.

Generated files:
- requirements_backup.txt: Original requirements saved before upgrades.
- requirements.txt: Updated, secure package versions pinned for Python 3.14.
- report.json: A short report listing packages that were changed and reasons.
- Dockerfile: Environment replication image for Linux.
- setup.sh: Create and populate .venv (Linux/macOS).
- run_test.sh: Run tests inside .venv (Linux/macOS).
- run_test.bat: Run tests inside .venv (Windows).
- auto_test.py: Automates venv creation, dependency installation, test execution, log collection and README updates.
- .gitignore: Updated to ignore .venv and logs.
- logs/: Directory written by auto_test.py with test_run.log.

How to set up the environment

Linux/macOS:
1. In project root: bash setup.sh
2. Activate: source .venv/bin/activate
3. Run tests: ./run_test.sh

Windows (PowerShell):
1. python -m venv .venv
2. .venv\Scripts\Activate.ps1
3. python -m pip install --upgrade pip setuptools wheel
4. pip install -r requirements.txt
5. run tests: .venv\Scripts\python.exe tests\case_1.py (or use run_test.bat)

Docker:
1. docker build -t project:test .
2. docker run --rm project:test

Using auto_test.py
1. python auto_test.py
2. The script will create a fresh .venv, install dependencies, run all scripts in tests/, write logs to logs/test_run.log, and append environment metadata to README.md.

Checking logs
- See logs/test_run.log for a detailed run output and return codes for each test script.

Environment created by automated process:
- Name: .venv
- Path: ./.venv
- Python: Python 3.14.0
- Pip: pip 25.3


Environment:
Path: D:\projects\v-JianzhangDong_25_12_09_case1\oswe-mini-m22a3s400\v-JianzhangDong_25_12_09_case1\.venv
Python: Python 3.14.0
Pip: pip 25.3 from D:\projects\v-JianzhangDong_25_12_09_case1\oswe-mini-m22a3s400\v-JianzhangDong_25_12_09_case1\.venv\Lib\site-packages\pip (python 3.14)
