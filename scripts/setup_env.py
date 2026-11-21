import subprocess
import sys
import os

def check_python():
    try:
        result = subprocess.run(['python3', '--version'], capture_output=True, text=True, check=True)
        print(f'Python version: {result.stdout.strip()}')
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

if __name__ == '__main__':
    if check_python():
        print('Python3 is already installed and accessible.')
        sys.exit(0)
    else:
        print('Error: python3 not found. Please ensure the environment is configured correctly.')
        sys.exit(1)