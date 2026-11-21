#!/bin/bash
set -e

# Check for Python3 and pip3
if ! command -v python3 &> /dev/null; then
    echo "Installing python3..."
    sudo apt-get update && sudo apt-get install -y python3 python3-pip
fi

# Install Python dependencies
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
fi

# Ensure Node.js dependencies are installed
npm install --include=dev

echo "Environment setup complete."
python3 --version
npx jest --version
