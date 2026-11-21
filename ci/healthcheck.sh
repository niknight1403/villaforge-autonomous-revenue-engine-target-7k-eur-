#!/bin/bash
# CI Health Check for Autonomous Revenue Engine

echo "Starting Environment Health Check..."

# Check required binaries
REQUIRED_COMMANDS=("python3" "pip" "node" "npm")

for cmd in "${REQUIRED_COMMANDS[@]}"; do
  if ! command -v "$cmd" &> /dev/null; then
    echo "Error: $cmd is not installed or not in PATH."
    exit 1
  fi
done

# Verify Node modules exist
if [ ! -d "node_modules" ]; then
  echo "Warning: node_modules not found. Running npm install..."
  npm install || exit 1
fi

# Verify Python requirements
if [ -f "requirements.txt" ]; then
  python3 -m pip install -r requirements.txt --quiet || exit 1
fi

echo "Environment Health Check passed successfully."
exit 0