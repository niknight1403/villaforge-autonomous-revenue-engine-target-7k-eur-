#!/bin/bash
# Pre-flight check for Autonomous Revenue Engine

echo "[Pre-Flight] Validating environment..."

if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed."
    exit 1
fi

if ! python3 -m pip --version &> /dev/null; then
    echo "Error: pip is not available for python3."
    exit 1
fi

echo "[Pre-Flight] Environment OK."
exit 0