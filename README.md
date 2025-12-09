# Project environment & automated test runner

This workspace contains dependency fixes, environment replication scripts, and an automated test runner to help reproduce and validate the build/test environment.

## ✅ What I changed / added

- `requirements.txt` — updated with pinned, current, stable package versions compatible with Python 3.14
- `requirements_backup.txt` — a safe copy of the original requirements
- `report.json` — a simplified report listing the dependency changes and reasons
- `.venv/` — virtual environment created (not committed), used for running tests
- `.gitignore` — added to ignore `.venv/`, `logs/` and editor artifacts
- `Dockerfile` — reproducible container using Python 3.14 and the pinned `requirements.txt`
- `setup.sh` — Linux/macOS helper to create a fresh `.venv` and install packages
- `run_test.sh` / `run_test.bat` — platform scripts to run tests and append results to `logs/test_run.log`
- `auto_test.py` — automatic test runner (detects .venv, runs tests in `tests/`, writes logs, updates `README.md`)
- `logs/test_run.log` — test execution log (created when tests were run locally)

---

## ⚙️ Setup (Linux / macOS)

1. Create a fresh virtual environment and install deps (script will delete and recreate `.venv` if present):

```bash
./setup.sh
```

2. Run tests manually (writes to `logs/test_run.log`):

```bash
./run_test.sh
```

## ⚙️ Setup & run (Windows PowerShell)

1. (Optional) Delete existing `.venv` then create a new one and install deps:

```powershell
if (Test-Path .venv) { Remove-Item -Recurse -Force .venv }
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip setuptools wheel
.\.venv\Scripts\python -m pip install -r requirements.txt
```

2. Run tests (Windows batch):

```powershell
run_test.bat
```

---

## 🧪 Using the automatic runner

The repository includes `auto_test.py` which:

- Detects `.venv` and uses the Python executable inside it
- Runs every `tests/*.py` and appends stdout/stderr and exit codes to `logs/test_run.log`
- Appends minor environment info (environment name, absolute path, Python/pip versions) into this `README.md`

Run it like:

```bash
.\.venv\Scripts\python auto_test.py   # Windows
./.venv/bin/python auto_test.py         # Linux/macOS
```

---

## 📂 Where to look for results

- Test output and failures are recorded in `logs/test_run.log`.
- Dependency change information is in `report.json`.
- The original dependency manifest is preserved as `requirements_backup.txt`.

---

Below are environment records written by `auto_test.py` (appended automatically):

Environment: .venv
Absolute path: D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\oswe-mini-secondary\v-JianzhangDong_25_12_09_case1\.venv
Python: Python 3.14.0
Pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\oswe-mini-secondary\v-JianzhangDong_25_12_09_case1\.venv\Lib\site-packages\pip (python 3.14)

Environment: .venv
Absolute path: D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\oswe-mini-secondary\v-JianzhangDong_25_12_09_case1\.venv
Python: Python 3.14.0
Pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\oswe-mini-secondary\v-JianzhangDong_25_12_09_case1\.venv\Lib\site-packages\pip (python 3.14)

Environment: .venv
Absolute path: D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\oswe-mini-secondary\v-JianzhangDong_25_12_09_case1\.venv
Python: Python 3.14.0
Pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\oswe-mini-secondary\v-JianzhangDong_25_12_09_case1\.venv\Lib\site-packages\pip (python 3.14)

Environment: .venv
Absolute path: D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\oswe-mini-secondary\v-JianzhangDong_25_12_09_case1\.venv
Python: Python 3.14.0
Pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\oswe-mini-secondary\v-JianzhangDong_25_12_09_case1\.venv\Lib\site-packages\pip (python 3.14)

# Project environment & automated test runner

This workspace contains dependency fixes, environment replication scripts, and an automated test runner to help reproduce and validate the build/test environment.

## ✅ What I changed / added

- `requirements.txt` — updated with pinned, current, stable package versions compatible with Python 3.14
- `requirements_backup.txt` — a safe copy of the original requirements
- `report.json` — a simplified report listing the dependency changes and reasons
- `.venv/` — virtual environment created (not committed), used for running tests
- `.gitignore` — added to ignore `.venv/`, `logs/` and editor artifacts
- `Dockerfile` — reproducible container using Python 3.14 and the pinned `requirements.txt`
- `setup.sh` — Linux/macOS helper to create a fresh `.venv` and install packages
- `run_test.sh` / `run_test.bat` — platform scripts to run tests and append results to `logs/test_run.log`
- `auto_test.py` — automatic test runner (detects .venv, runs tests in `tests/`, writes logs, updates `README.md`)
- `logs/test_run.log` — test execution log (created when tests were run locally)

---

## ⚙️ Setup (Linux / macOS)

1. Create a fresh virtual environment and install deps (script will delete and recreate `.venv` if present):

```bash
./setup.sh
```

2. Run tests manually (writes to `logs/test_run.log`):

```bash
./run_test.sh
```

## ⚙️ Setup & run (Windows PowerShell)

1. (Optional) Delete existing `.venv` then create a new one and install deps:

```powershell
if (Test-Path .venv) { Remove-Item -Recurse -Force .venv }
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip setuptools wheel
.\.venv\Scripts\python -m pip install -r requirements.txt
```

2. Run tests (Windows batch):

```powershell
run_test.bat
```

---

## 🧪 Using the automatic runner

The repository includes `auto_test.py` which:

- Detects `.venv` and uses the Python executable inside it
- Runs every `tests/*.py` and appends stdout/stderr and exit codes to `logs/test_run.log`
- Appends minor environment info (environment name, absolute path, Python/pip versions) into this `README.md`

Run it like:

```bash
.\.venv\Scripts\python auto_test.py   # Windows
./.venv/bin/python auto_test.py         # Linux/macOS
```

---

## 📂 Where to look for results

- Test output and failures are recorded in `logs/test_run.log`.
- Dependency change information is in `report.json`.
- The original dependency manifest is preserved as `requirements_backup.txt`.

---

Below are environment records written by `auto_test.py` (appended automatically):
