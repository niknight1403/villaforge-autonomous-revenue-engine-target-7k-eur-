import os
import sys
import subprocess
import time

def check_environment():
    if subprocess.call(['which', 'python3'], stdout=subprocess.DEVNULL) != 0:
        print('Error: python3 not found')
        sys.exit(1)
    if subprocess.call(['which', 'node'], stdout=subprocess.DEVNULL) != 0:
        print('Error: node not found')
        sys.exit(1)

def run_build_with_retry(command_str, retries=3):
    command = command_str.split(' && ')
    for i in range(retries):
        try:
            for cmd in command:
                subprocess.check_call(cmd.split())
            return True
        except subprocess.CalledProcessError:
            wait = 2 ** i
            print(f'Build failed, retrying in {wait}s...')
            time.sleep(wait)
    return False

if __name__ == '__main__':
    check_environment()
    if not run_build_with_retry('pip install -r requirements.txt && npm install'):
        print('Critical: Build failed after retries.')
        sys.exit(1)
    print('Pre-commit guard passed.')