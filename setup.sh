#!/bin/bash

# setup.sh - Environment setup script for Linux/macOS

set -e

echo "=========================================="
echo "Setting up Python environment"
echo "=========================================="

# Check Python version
echo "Checking Python version..."
python3 --version

# Check pip version
echo "Checking pip version..."
pip3 --version

# Remove existing venv if present
if [ -d ".venv" ]; then
    echo "Removing existing .venv directory..."
    rm -rf .venv
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Display installed packages
echo "=========================================="
echo "Installed packages:"
echo "=========================================="
pip list

# Create logs directory
if [ ! -d "logs" ]; then
    echo "Creating logs directory..."
    mkdir -p logs
fi

echo "=========================================="
echo "Environment setup complete!"
echo "To activate the environment, run:"
echo "source .venv/bin/activate"
echo "=========================================="
