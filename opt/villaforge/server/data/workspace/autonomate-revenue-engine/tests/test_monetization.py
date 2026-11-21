import unittest


class TestMonetization(unittest.TestCase):
    def test_calculate_revenue(self):
        from src.main import calculate_revenue
        data = {'subscriptions': [{'plan': 'basic', 'users': 2}, {'plan': 'pro', 'users': 1}]}
        self.assertEqual(calculate_revenue(data), 300)

if __name__ == '__main__':
    unittest.main()