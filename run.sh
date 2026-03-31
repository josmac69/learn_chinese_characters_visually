#!/bin/bash

# Exit on any error
set -e

# Name of the virtual environment directory
VENV_DIR="venv"

# 1. Check if the virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in '$VENV_DIR'..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created successfully."
else
    echo "Using existing virtual environment in '$VENV_DIR'."
fi

# 2. Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# 3. Start the application
echo "Starting application..."
python main.py

# Deactivate after closing (optional, mostly useful if run with 'source run.sh')
deactivate 2>/dev/null || true
