#!/bin/bash
# Pre-flight check for Autonomous Revenue Engine

echo "[Pre-flight] Checking environment and Python syntax..."

# 1. Check for python3
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 is not installed or not in PATH."
    exit 1
fi

# 2. Compile all python files to check syntax
PY_FILES=$(find src -name "*.py")
for f in $PY_FILES; do
    python3 -m py_compile "$f"
    if [ $? -ne 0 ]; then
        echo "[ERROR] Syntax error in $f"
        exit 1
    fi
done

echo "[Success] Environment and syntax check passed."
exit 0