#!/usr/bin/env python3

import os
import sys
import subprocess
import datetime

def main():
    # Detect environment
    venv_path = os.path.join(os.getcwd(), '.venv')
    if not os.path.exists(venv_path):
        print("Virtual environment .venv not found.")
        sys.exit(1)

    # Python executable in venv
    python_exe = os.path.join(venv_path, 'Scripts', 'python.exe') if os.name == 'nt' else os.path.join(venv_path, 'bin', 'python')

    # Get versions
    try:
        result = subprocess.run([python_exe, '--version'], capture_output=True, text=True)
        python_version = result.stdout.strip()
    except:
        python_version = "Unknown"

    try:
        result = subprocess.run([python_exe, '-m', 'pip', '--version'], capture_output=True, text=True)
        pip_version = result.stdout.strip().split()[1]
    except:
        pip_version = "Unknown"

    # Create logs directory
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    log_file = os.path.join(logs_dir, 'test_run.log')

    with open(log_file, 'w') as f:
        f.write(f"Test run started at {datetime.datetime.now()}\n")
        f.write(f"Environment: .venv\n")
        f.write(f"Path: {venv_path}\n")
        f.write(f"Python version: {python_version}\n")
        f.write(f"Pip version: {pip_version}\n\n")

        # Run tests
        test_dir = 'tests'
        if os.path.exists(test_dir):
            for test_file in os.listdir(test_dir):
                if test_file.endswith('.py'):
                    test_path = os.path.join(test_dir, test_file)
                    f.write(f"Running {test_file}...\n")
                    try:
                        env = os.environ.copy()
                        env['PYTHONPATH'] = os.getcwd()
                        result = subprocess.run([python_exe, test_path], capture_output=True, text=True, cwd=os.getcwd(), env=env)
                        f.write(result.stdout)
                        if result.stderr:
                            f.write("STDERR:\n" + result.stderr)
                        f.write(f"Return code: {result.returncode}\n\n")
                    except Exception as e:
                        f.write(f"Error running {test_file}: {e}\n\n")
        else:
            f.write("Tests directory not found.\n")

    # Append to README.md
    readme_path = 'README.md'
    with open(readme_path, 'a') as f:
        f.write(f"\nEnvironment: .venv\n")
        f.write(f"Path: {venv_path}\n")
        f.write(f"Python version: {python_version}\n")
        f.write(f"Pip version: {pip_version}\n")

    print(f"Tests completed. Results written to {log_file}")

if __name__ == "__main__":
    main()