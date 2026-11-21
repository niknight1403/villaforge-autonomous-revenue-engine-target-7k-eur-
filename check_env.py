import sys
import os

def check_environment():
    print(f'Python version: {sys.version}')
    print(f'Executable: {sys.executable}')
    if os.path.exists('/usr/bin/python3'):
        print('Path /usr/bin/python3 exists.')
    else:
        print('Path /usr/bin/python3 missing.')

if __name__ == '__main__':
    check_environment()