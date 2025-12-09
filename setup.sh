#!/usr/bin/env bash
set -euo pipefail

# Create or recreate a clean virtual environment at .venv/
if [ -d ".venv" ]; then
  echo "Removing existing .venv/"
  rm -rf .venv
fi
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Virtual environment ready at $(pwd)/.venv"
