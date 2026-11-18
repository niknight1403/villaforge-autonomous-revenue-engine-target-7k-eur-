import py_compile
import sys

try:
    py_compile.compile('src/app.py', doraise=True)
    print('Build successful')
except Exception as e:
    print(f'Build failed: {e}')
    sys.exit(1)