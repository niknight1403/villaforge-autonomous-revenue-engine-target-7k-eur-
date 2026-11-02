import unittest

class TestMonetization(unittest.TestCase):
    def test_calculate_revenue(self):
        self.assertEqual(calculate_revenue(100, 0.1), 10)

if __name__ == '__main__':
    unittest.main()