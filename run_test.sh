#!/usr/bin/env bash
set -euo pipefail

if [ ! -d ".venv" ]; then
  echo ".venv not found. Run setup.sh first."
  exit 1
fi

source .venv/bin/activate
export PYTHONPATH="$(pwd)"
mkdir -p logs
python -u -c "import sys, pathlib; print('Python', sys.version)\nprint('Running tests in tests/ folder')"

for f in tests/*.py; do
  echo "----- Running $f -----"
  python "$f" || true
done

echo "Done. Logs are in logs/test_run.log (see auto_test.py for automated logging)."
