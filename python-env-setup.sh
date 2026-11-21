#!/bin/bash
# Standardisierung der Runtime-Umgebung

if ! command -v python3 &> /dev/null; then
    echo "python3 nicht gefunden. Bitte installieren."
    exit 1
fi

if [ ! -d "venv" ]; then
    echo "Erstelle venv..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

echo "Umgebung bereit: $(which python3)"
