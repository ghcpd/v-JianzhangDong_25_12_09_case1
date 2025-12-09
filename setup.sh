#!/bin/bash

# Setup script for Linux/macOS

echo "Setting up Python environment..."

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python is not installed. Please install Python 3.14 or later."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.14.0"

if [[ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]]; then
    echo "Python version $PYTHON_VERSION is not supported. Please upgrade to Python 3.14 or later."
    exit 1
fi

# Create virtual environment
if [ -d ".venv" ]; then
    rm -rf .venv
fi

python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Environment setup complete."