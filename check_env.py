import sys
import os

def check_environment():
    print(f'Python version: {sys.version}')
    print(f'Executable: {sys.executable}')
    print(f'Path: {os.environ.get("PATH", "Not set")}')
    return 0

if __name__ == '__main__':
    sys.exit(check_environment())