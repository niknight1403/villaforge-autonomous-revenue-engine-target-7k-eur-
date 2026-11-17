import unittest
from src.monetization import calculate_mrr

class TestMonetization(unittest.TestCase):
    def test_calculate_mrr_basic(self):
        # Test with 10 users at 50 EUR each
        users = 10
        price = 50
        expected = 500
        self.assertEqual(calculate_mrr(users, price), expected)

    def test_calculate_mrr_zero(self):
        self.assertEqual(calculate_mrr(0, 50), 0)

    def test_calculate_mrr_negative(self):
        with self.assertRaises(ValueError):
            calculate_mrr(-1, 50)

if __name__ == '__main__':
    unittest.main()