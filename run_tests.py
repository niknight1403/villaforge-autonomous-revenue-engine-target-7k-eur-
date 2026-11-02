import unittest
import sys
import os

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='tests')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == '__main__':
    run_tests()