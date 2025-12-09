#!/usr/bin/env bash
set -euo pipefail

# Remove any existing .venv to ensure a clean environment
if [ -d ".venv" ]; then
  echo "Removing existing .venv..."
  rm -rf .venv
fi

python -m venv .venv
echo "Created virtual environment .venv"

source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Environment set up in .venv. Use 'source .venv/bin/activate' to activate."
