import unittest
from src.main import calculate_revenue

class TestRevenueEngine(unittest.TestCase):
    def test_calculate_revenue(self):
        data = {
            'subscriptions': [
                {'plan': 'basic', 'users': 2},
                {'plan': 'pro', 'users': 1},
                {'plan': 'enterprise', 'users': 0}
            ]
        }
        # 2 * 50 + 1 * 200 = 300
        self.assertEqual(calculate_revenue(data), 300)

if __name__ == '__main__':
    unittest.main()