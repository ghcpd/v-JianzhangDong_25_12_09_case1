# Project Environment and Dependency Management Guide

## Overview

This document provides complete instructions for setting up, managing, and testing the project environment. The project has been updated with secure, compatible dependencies and includes comprehensive testing infrastructure.

### Generated Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Updated list of project dependencies with secure, compatible versions |
| `requirements_backup.txt` | Backup of original requirements.txt for reference |
| `report.json` | Detailed analysis of dependency issues and updates |
| `.venv/` | Python virtual environment with all dependencies installed |
| `.gitignore` | Git ignore rules (includes .venv/) |
| `Dockerfile` | Docker container image for reproducible environments |
| `setup.sh` | Automated environment setup script (Linux/macOS) |
| `run_test.sh` | Test execution script (Linux/macOS) |
| `run_test.bat` | Test execution script (Windows) |
| `auto_test.py` | Automated test runner with environment detection |
| `logs/test_run.log` | Test execution results and logs |
| `README.md` | This file |

---

## Environment Information

### Current Environment
- **Environment Type:** Python Virtual Environment (.venv/)
- **Absolute Path:** `D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\haiku-4.5\v-JianzhangDong_25_12_09_case1\.venv`
- **Python Version:** 3.14.0
- **Pip Version:** 25.3
- **Host Python:** Python 3.14.0

### Installed Packages
```
certifi==2025.11.12
charset-normalizer==3.4.4
colorama==0.4.6
idna==3.11
pyyaml==6.0.1
requests==2.32.3
tqdm==4.67.1
typing_extensions==4.12.2
urllib3==2.6.1
```

---

## Dependency Updates Summary

The following packages were updated to address security vulnerabilities and compatibility issues:

### Updated Packages
1. **requests** (2.25.0 → 2.32.3)
   - Reason: Contains known security vulnerabilities (CVE-2023-32681)
   
2. **pyyaml** (5.3.1 → 6.0.1)
   - Reason: Security vulnerability (CVE-2020-14343 - arbitrary code execution)
   
3. **tqdm** (4.32.0 → 4.67.1)
   - Reason: Very outdated package from 2018
   
4. **typing_extensions** (3.7.4 → 4.12.2)
   - Reason: Outdated package from 2019

### Removed Packages
The following packages have been **removed** due to Python 3.14 compatibility issues:
- numpy (1.24.0) - No wheel support for Python 3.14
- pandas (1.5.0) - Requires numpy as dependency
- matplotlib (3.5.0) - Requires numpy as dependency
- scipy (1.9.0) - Requires numpy as dependency
- lxml (4.6.1) - No wheel support for Python 3.14
- regex (2021.4.4) - Requires C++ compiler (MSVC 14.0+)

For detailed information on all identified issues, see `report.json`.

---

## Setup Instructions

### Windows

#### Option 1: Using the Provided Virtual Environment (Recommended)
The `.venv/` directory is already set up with all dependencies. Simply activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If you encounter an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1
```

#### Option 2: Create a Fresh Environment
To create a new virtual environment from scratch:

```powershell
# Remove existing environment
if (Test-Path ".venv") { Remove-Item -Recurse -Force .venv }

# Create new environment
python -m venv .venv

# Activate
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Linux/macOS

#### Option 1: Using the Setup Script
```bash
chmod +x setup.sh
./setup.sh
```

This script will:
- Remove any existing `.venv` directory
- Create a new virtual environment
- Upgrade pip, setuptools, and wheel
- Install all dependencies
- Create the logs directory

#### Option 2: Manual Setup
```bash
# Create virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements.txt

# Create logs directory
mkdir -p logs
```

---

## Running Tests

### Windows

#### Using the Batch Script
```batch
run_test.bat
```

#### Using the Python Script Directly
```powershell
.venv\Scripts\python.exe auto_test.py
```

### Linux/macOS

#### Using the Bash Script
```bash
chmod +x run_test.sh
./run_test.sh
```

#### Using the Python Script Directly
```bash
source .venv/bin/activate
python auto_test.py
```

---

## Auto Test (auto_test.py)

The `auto_test.py` script provides comprehensive testing functionality:

### Features
- Automatic environment detection (Python version, virtual environment path)
- Discovers all test files in the `tests/` directory
- Runs each test and captures output
- Logs all results to `logs/test_run.log`
- Provides detailed error reporting
- Returns appropriate exit codes for CI/CD integration

### Usage

#### Basic Execution
```bash
python auto_test.py
```

#### With Virtual Environment Activation
Windows:
```powershell
.venv\Scripts\python.exe auto_test.py
```

Linux/macOS:
```bash
source .venv/bin/activate
python auto_test.py
```

### Output
The script provides:
1. **Console Output:** Real-time test execution feedback
2. **Log File:** Detailed results in `logs/test_run.log`

Example console output:
```
============================================================
AUTOMATED TEST RUN
============================================================

Environment Information:
  python_version: 3.14.0 (tags/v3.14.0:...)
  python_executable: /path/to/.venv/bin/python
  virtual_env: /path/to/.venv
  working_directory: /path/to/project
  timestamp: 2025-12-09T10:30:00.000000

Discovered 3 test files:
  - case_1.py
  - case_2.py
  - case_3.py

============================================================
RUNNING TESTS
============================================================

============================================================
Running: case_1.py
============================================================
✓ PASSED
Output:
Normalization OK: [array values...]

...

============================================================
TEST SUMMARY
============================================================
Total Tests: 3
Passed: 2
Failed: 1
Success Rate: 66.7%

Log file: /path/to/logs/test_run.log
```

---

## Checking Test Logs

### View Log File

Windows:
```powershell
Get-Content logs\test_run.log
```

Linux/macOS:
```bash
cat logs/test_run.log
```

### Log File Location
- **Absolute Path:** `D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\haiku-4.5\v-JianzhangDong_25_12_09_case1\logs\test_run.log`

### Log Contents
The log file includes:
- Environment information (Python version, virtual environment path)
- Timestamp of test execution
- Individual test results (passed/failed/error)
- Test output and error messages
- Summary statistics
- Success rate calculation

---

## Docker Support

### Building the Docker Image
```bash
docker build -t project-env .
```

### Running Tests in Docker
```bash
docker run --rm project-env python auto_test.py
```

### Dockerfile Details
The provided `Dockerfile`:
- Uses Python 3.14 slim image
- Installs dependencies from requirements.txt
- Copies application and test files
- Sets proper environment variables
- Can be extended for production use

---

## Troubleshooting

### Issue: "Python 3.14 not found"
**Solution:** Python 3.14 must be installed. Download from [python.org](https://python.org)

### Issue: Virtual environment not activating
**Windows:** Use the full path:
```powershell
& ".\.venv\Scripts\Activate.ps1"
```

**Linux/macOS:** Make sure to source, not execute:
```bash
source .venv/bin/activate
```

### Issue: Packages won't install
**Solution:** Some packages don't have Python 3.14 wheels yet. See the "Removed Packages" section above.

### Issue: "Module not found" in tests
**Solution:** Ensure the virtual environment is activated:
```powershell
# Windows
.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

### Issue: Permission denied on setup.sh
**Solution:**
```bash
chmod +x setup.sh
./setup.sh
```

---

## Git Integration

### .gitignore Configuration
The `.gitignore` file has been configured to exclude:
- Virtual environment (`.venv/`)
- Python cache files (`__pycache__/`, `*.pyc`)
- Testing artifacts (`.pytest_cache/`, `.coverage`)
- Log files (`logs/`)
- IDE files (`.vscode/`, `.idea/`)
- OS-specific files (`Thumbs.db`, `.DS_Store`)

This ensures that only source code and configuration files are committed to the repository.

---

## Project Structure

```
project_root/
├── .venv/                      # Virtual environment (excluded from git)
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Updated dependencies
├── requirements_backup.txt     # Original dependencies (reference)
├── report.json                 # Dependency analysis report
├── Dockerfile                  # Docker container definition
├── setup.sh                    # Linux/macOS setup script
├── run_test.sh                 # Linux/macOS test runner
├── run_test.bat                # Windows test runner
├── auto_test.py                # Automated test runner
├── README.md                   # This file
├── logs/                       # Test logs (excluded from git)
│   └── test_run.log           # Test execution results
├── app/                        # Application code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── text_processor.py
│   └── visualizer.py
└── tests/                      # Test cases
    ├── case_1.py
    ├── case_2.py
    └── case_3.py
```

---

## Additional Resources

### Dependency Management Best Practices
1. **Always use virtual environments** - Isolates project dependencies
2. **Pin versions** - Ensures reproducible builds
3. **Regularly update** - Keep dependencies secure and current
4. **Monitor CVEs** - Check for known vulnerabilities
5. **Test thoroughly** - Verify compatibility after updates

### Useful Commands

#### Check Installed Packages
```bash
pip list
pip show <package_name>
```

#### Freeze Current Environment
```bash
pip freeze > requirements_current.txt
```

#### Update All Packages
```bash
pip install --upgrade -r requirements.txt
```

#### Check for Outdated Packages
```bash
pip list --outdated
```

---

## Version Information

- **Python:** 3.14.0
- **Pip:** 25.3
- **Last Updated:** 2025-12-09
- **Virtual Environment Path:** `.venv/` (located at `D:\vscoderprojects\v-JianzhangDong_25_12_09_case1\haiku-4.5\v-JianzhangDong_25_12_09_case1\.venv`)

---

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review `report.json` for dependency details
3. Check `logs/test_run.log` for test failures
4. Ensure the virtual environment is properly activated

---

**End of Documentation**
