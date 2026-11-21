#!/bin/bash

# Pre-flight check script for Autonomous Revenue Engine
# Ensures environment meets minimum requirements before build/test

echo "[Pre-Flight] Checking environment..."

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 is not installed or not in PATH."
    exit 1
fi

# Check for required python modules
REQUIRED_MODULES=("flask" "stripe")
for module in "${REQUIRED_MODULES[@]}"; do
    if ! python3 -c "import $module" &> /dev/null; then
        echo "[ERROR] Required Python module '$module' is missing."
        exit 1
    fi
done

echo "[SUCCESS] Environment check passed."
exit 0
