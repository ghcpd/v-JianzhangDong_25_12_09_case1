Project environment and testing helper files

Generated files and purpose:
- requirements_backup.txt: Backup of the original requirements.txt
- requirements.txt: Updated, pinned dependency versions, compatible with Python 3.14
- report.json: Summary report of updated packages and reasons
- Dockerfile: Reproducible container using python:3.14-slim
- setup.sh: Creates a clean .venv and installs dependencies (Linux/macOS)
- run_test.sh: Activates .venv and runs auto_test.py (Linux/macOS)
- run_test.bat: Runs auto_test.py using .venv python (Windows)
- auto_test.py: Runs all test scripts (tests/*.py) using the .venv python and writes logs to logs/test_run.log; appends environment info to README.md
- logs/: Directory where test_run.log will be created
- .gitignore: Updated to ignore .venv/ and logs/

Setup instructions (Linux/macOS):
1. Ensure Python 3.14 is installed and available as python.
2. Make the scripts executable: chmod +x setup.sh run_test.sh
3. Run: ./setup.sh
4. To run tests: ./run_test.sh

Setup instructions (Windows):
1. Ensure Python 3.14 is installed and available on PATH.
2. Create the venv: python -m venv .venv
3. Upgrade pip and install dependencies: .venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
4. Install requirements: .venv\Scripts\python.exe -m pip install -r requirements.txt
5. To run tests: run_test.bat

Using auto_test.py directly:
- Activate the .venv and run: python auto_test.py
- This will execute all .py files in tests/, write results to logs/test_run.log, and append environment info to README.md.

Checking logs:
- The test run log is at logs/test_run.log. Each run appends a timestamped section with environment details and per-test output.


Environment: D:\projects\v-JianzhangDong_25_12_09_case1\oswe-mini-m22a5s270\v-JianzhangDong_25_12_09_case1\.venv
Absolute Path: D:\projects\v-JianzhangDong_25_12_09_case1\oswe-mini-m22a5s270\v-JianzhangDong_25_12_09_case1
Python 3.14.0
pip 25.3 from D:\projects\v-JianzhangDong_25_12_09_case1\oswe-mini-m22a5s270\v-JianzhangDong_25_12_09_case1\.venv\Lib\site-packages\pip (python 3.14)


Environment: D:\projects\v-JianzhangDong_25_12_09_case1\oswe-mini-m22a5s270\v-JianzhangDong_25_12_09_case1\.venv
Absolute Path: D:\projects\v-JianzhangDong_25_12_09_case1\oswe-mini-m22a5s270\v-JianzhangDong_25_12_09_case1
Python 3.14.0
pip 25.3 from D:\projects\v-JianzhangDong_25_12_09_case1\oswe-mini-m22a5s270\v-JianzhangDong_25_12_09_case1\.venv\Lib\site-packages\pip (python 3.14)
