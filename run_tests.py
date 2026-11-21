#!/usr/bin/env python3
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='*_test.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    exit(0 if result.wasSuccessful() else 1)
