import sys
import subprocess

print(f"Python version: {sys.version}")

# Check if pytest is available
result = subprocess.run(["python3", "-m", "pytest", "--version"], capture_output=True, text=True)
print(f"pytest output: {result.stdout}")
print(f"pytest stderr: {result.stderr}")
print(f"pytest return code: {result.returncode}")

# Try running the existing smoke test
result2 = subprocess.run(["python3", "scripts/smoke_test.py"], capture_output=True, text=True)
print(f"smoke test output: {result2.stdout}")
print(f"smoke test stderr: {result2.stderr}")
print(f"smoke test return code: {result2.returncode}")

# Check if index.html exists and has content
import os
if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    print(f"index.html size: {len(content)} bytes")
    print(f"index.html starts with: {content[:100]}")
else:
    print("index.html not found")

print("\n--- Test Complete ---")
