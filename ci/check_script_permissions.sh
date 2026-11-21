#!/bin/bash
# CI-Check: Validate that all files in ./scripts are executable

echo "Checking script permissions in ./scripts..."
NON_EXECUTABLE=$(find ./scripts -type f ! -executable)

if [ -n "$NON_EXECUTABLE" ]; then
  echo "ERROR: The following scripts are not executable:"
  echo "$NON_EXECUTABLE"
  exit 1
else
  echo "All scripts in ./scripts are executable."
  exit 0
fi