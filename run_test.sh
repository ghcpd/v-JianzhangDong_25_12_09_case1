#!/bin/bash

# Test runner script for Linux/macOS

echo "Running tests..."

# Activate virtual environment
source .venv/bin/activate

# Run tests
python -m pytest tests/ -v

echo "Tests completed."