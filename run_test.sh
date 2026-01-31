#!/usr/bin/env bash
set -euo pipefail

if [ ! -d ".venv" ]; then
  echo ".venv does not exist. Run setup.sh first to create the virtual environment."
  exit 1
fi
. .venv/bin/activate
python auto_test.py
