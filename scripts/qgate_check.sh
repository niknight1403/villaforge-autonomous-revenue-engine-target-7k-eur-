#!/bin/bash

check_runtime() {
    if ! command -v python3 &> /dev/null || ! command -v npm &> /dev/null; then
        echo "[ERROR] Umgebung unvollständig: Python3 oder Node.js nicht gefunden."
        echo "[INFO] Triggering setup..."
        ./scripts/setup.sh
        exit 1
    fi
    echo "[OK] Runtime Check erfolgreich."
}

check_runtime

if [ "$1" == "test" ]; then
    npm test
fi