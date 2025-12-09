#!/usr/bin/env bash
set -euo pipefail

# Create fresh virtual environment in .venv
if [ -d ".venv" ]; then
  echo "Removing existing .venv"
  rm -rf .venv
fi

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Virtual environment created at $(pwd)/.venv"
