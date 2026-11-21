import unittest
from src.engine import RevenueEngine

class TestRevenueEngine(unittest.TestCase):
    def test_calculate_mrr(self):
        engine = RevenueEngine()
        subs = [{'plan': 'basic', 'users': 10}, {'plan': 'pro', 'users': 2}]
        # 10 * 50 + 2 * 200 = 500 + 400 = 900
        self.assertEqual(engine.calculate_mrr(subs), 900)

    def test_target_gap(self):
        engine = RevenueEngine()
        self.assertEqual(engine.get_target_gap(900, 7000), 6100)

if __name__ == '__main__':
    unittest.main()