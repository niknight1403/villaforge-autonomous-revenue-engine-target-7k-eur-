#!/usr/bin/env python3

import os

def build_project():
    print('Building the project...')
    os.system('npm run build')

if __name__ == '__main__':
    build_project()