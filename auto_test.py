#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
VENV = ROOT / '.venv'

# Determine python executable inside .venv
def venv_python():
    # If running inside the desired venv already, use current executable
    cur = Path(sys.executable)
    if VENV in cur.parents or str(cur).startswith(str(VENV)):
        return str(cur)
    # Windows
    candidate = VENV / 'Scripts' / 'python.exe'
    if candidate.exists():
        return str(candidate)
    # POSIX
    candidate = VENV / 'bin' / 'python'
    if candidate.exists():
        return str(candidate)
    # Fall back to current python
    return str(cur)

PYTHON = venv_python()

LOGS = ROOT / 'logs'
LOGS.mkdir(exist_ok=True)
LOGFILE = LOGS / 'test_run.log'

def run_cmd(cmd):
    env = os.environ.copy()
    # Ensure tests can import the local package
    env['PYTHONPATH'] = str(ROOT)
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env)
    return p.returncode, p.stdout

# Gather environment info
ret, py_out = run_cmd([PYTHON, '--version'])
ret2, pip_out = run_cmd([PYTHON, '-m', 'pip', '--version'])
env_info = {
    'venv_path': str(VENV),
    'python': py_out.strip(),
    'pip': pip_out.strip(),
    'timestamp': datetime.utcnow().isoformat() + 'Z'
}

# Write header to log
with open(LOGFILE, 'a', encoding='utf-8') as f:
    f.write('\n===== Test run: {} =====\n'.format(env_info['timestamp']))
    f.write('Environment: {}\n'.format(env_info['venv_path']))
    f.write('Python: {}\n'.format(env_info['python']))
    f.write('Pip: {}\n\n'.format(env_info['pip']))

# Run each test script in tests/
TESTS_DIR = ROOT / 'tests'
any_fail = False
if TESTS_DIR.exists():
    for p in sorted(TESTS_DIR.iterdir()):
        if p.is_file() and p.suffix == '.py':
            with open(LOGFILE, 'a', encoding='utf-8') as f:
                f.write('--- Running: {} ---\n'.format(p.name))
            cmd = [PYTHON, str(p)]
            rc, out = run_cmd(cmd)
            with open(LOGFILE, 'a', encoding='utf-8') as f:
                f.write(out)
                f.write('\nReturn code: {}\n\n'.format(rc))
            if rc != 0:
                any_fail = True
else:
    with open(LOGFILE, 'a', encoding='utf-8') as f:
        f.write('No tests directory found.\n')

# Append environment info to README.md
README = ROOT / 'README.md'
append_text = ('\nEnvironment: {venv_path}\nAbsolute Path: {abs_path}\n{python}\n{pip}\n'.format(
    venv_path=env_info['venv_path'],
    abs_path=str(ROOT),
    python=env_info['python'],
    pip=env_info['pip']
))
with open(README, 'a', encoding='utf-8') as f:
    f.write('\n' + append_text)

if any_fail:
    print('Some tests failed. See logs/test_run.log for details.')
    sys.exit(1)
else:
    print('All tests completed. See logs/test_run.log for details.')
    sys.exit(0)
