import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from optimization import run_optimization, calculate_mrr

class TestOptimization(unittest.TestCase):
    def test_calculate_mrr(self):
        mrr = calculate_mrr(100, 59)
        self.assertEqual(mrr, 5900)

    def test_run_optimization(self):
        result = run_optimization()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
