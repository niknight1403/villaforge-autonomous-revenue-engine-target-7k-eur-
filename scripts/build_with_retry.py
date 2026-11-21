import subprocess
import time
import sys

def build_with_retry(command, max_retries=3):
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1} of {max_retries} for command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print("Build successful.")
            return True
        print(f"Attempt {attempt + 1} failed: {result.stderr}")
        time.sleep(2 ** attempt)
    print("Build failed after maximum retries.")
    return False

if __name__ == '__main__':
    if not build_with_retry(['pip', 'install', '-r', 'requirements.txt']):
        sys.exit(1)
    if not build_with_retry(['npm', 'install']):
        sys.exit(1)
    sys.exit(0)