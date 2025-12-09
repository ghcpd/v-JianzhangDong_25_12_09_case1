#!/usr/bin/env bash
set -euo pipefail

# Ensure logs directory exists
mkdir -p logs
LOGFILE=logs/test_run.log
echo "Running tests at $(date --iso-8601=seconds)" >> "$LOGFILE"

# If .venv exists, use it; otherwise use system python
if [ -d ".venv" ]; then
  echo "Using .venv Python to run tests" >> "$LOGFILE"
  . .venv/bin/activate
  PYTHON=".venv/bin/python"
else
  echo "No .venv found, using system Python" >> "$LOGFILE"
  PYTHON="python"
fi

export PYTHONPATH="$PWD"
for f in tests/*.py; do
  echo "--- Running $f ---" | tee -a "$LOGFILE"
  $PYTHON "$f" 2>&1 | tee -a "$LOGFILE"
done

echo "Tests completed at $(date --iso-8601=seconds)" >> "$LOGFILE"
