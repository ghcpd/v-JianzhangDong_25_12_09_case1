#!/bin/bash

# run_test.sh - Test execution script for Linux/macOS

set -e

echo "=========================================="
echo "Running tests on Linux/macOS"
echo "=========================================="

# Check if .venv exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found at .venv"
    echo "Please run setup.sh first"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Display environment info
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

# Create logs directory if it doesn't exist
mkdir -p logs

# Run auto_test.py
echo "Executing auto_test.py..."
python auto_test.py

echo "=========================================="
echo "Tests completed. Check logs/test_run.log"
echo "=========================================="
