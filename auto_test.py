#!/usr/bin/env python3
"""Auto-run tests using the repository .venv and log outputs.

This script will:
 - detect .venv python executable
 - run each Python file in the tests/ folder with the chosen Python
 - append results to logs/test_run.log
 - append environment details (name, absolute path, python/pip versions) to README.md
"""
import os
import subprocess
import sys
from datetime import datetime


ROOT = os.path.abspath(os.path.dirname(__file__))
VENV = os.path.join(ROOT, '.venv')
LOG_DIR = os.path.join(ROOT, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOGFILE = os.path.join(LOG_DIR, 'test_run.log')


def detect_venv_python():
    # Windows vs POSIX
    win_path = os.path.join(VENV, 'Scripts', 'python.exe')
    posix_path = os.path.join(VENV, 'bin', 'python')
    if os.path.exists(win_path):
        return win_path
    if os.path.exists(posix_path):
        return posix_path
    return None


def get_version_info(python_exe):
    try:
        py_ver = subprocess.check_output([python_exe, '--version'], stderr=subprocess.STDOUT).decode().strip()
    except Exception:
        py_ver = 'unknown'
    try:
        pip_ver = subprocess.check_output([python_exe, '-m', 'pip', '--version'], stderr=subprocess.STDOUT).decode().strip()
    except Exception:
        pip_ver = 'unknown'
    return py_ver, pip_ver


def main():
    python_exe = detect_venv_python()
    if python_exe is None:
        print('No .venv environment found. Please run setup.sh / create .venv first.')
        sys.exit(2)

    py_ver, pip_ver = get_version_info(python_exe)

    with open(LOGFILE, 'a', encoding='utf-8') as out:
        out.write(f"\n=== Test run started: {datetime.now().isoformat()} ===\n")
        out.write(f"Using environment: .venv -> {python_exe}\n")
        out.write(f"Python: {py_ver}\n")
        out.write(f"Pip: {pip_ver}\n\n")

    tests_dir = os.path.join(ROOT, 'tests')
    if not os.path.isdir(tests_dir):
        print('No tests/ directory found. Nothing to run.')
        sys.exit(0)

    test_files = sorted([f for f in os.listdir(tests_dir) if f.endswith('.py')])
    if not test_files:
        print('No test files found in tests/.')
        sys.exit(0)

    for tf in test_files:
        full = os.path.join(tests_dir, tf)
        with open(LOGFILE, 'a', encoding='utf-8') as out:
            out.write(f"--- Running {tf} ---\n")
        try:
            # ensure the repository root is on sys.path when executing tests so imports like `from app` work
            env = os.environ.copy()
            env['PYTHONPATH'] = ROOT
            proc = subprocess.run([python_exe, full], capture_output=True, text=True, check=False, cwd=ROOT, env=env)
            with open(LOGFILE, 'a', encoding='utf-8') as out:
                out.write(proc.stdout)
                if proc.stderr:
                    out.write('\n-- STDERR --\n')
                    out.write(proc.stderr)
                out.write(f"\nExit code: {proc.returncode}\n\n")
        except Exception as exc:
            with open(LOGFILE, 'a', encoding='utf-8') as out:
                out.write('Execution failed: ' + str(exc) + '\n')

    # append environment info to README.md
    readme_path = os.path.join(ROOT, 'README.md')
    with open(readme_path, 'a', encoding='utf-8') as r:
        r.write('\n---\n')
        r.write(f"Environment: .venv\n")
        r.write(f"Absolute path: {VENV}\n")
        r.write(f"Python: {py_ver}\n")
        r.write(f"Pip: {pip_ver}\n")

    print('Tests executed. Results are appended to', LOGFILE)


if __name__ == '__main__':
    main()
