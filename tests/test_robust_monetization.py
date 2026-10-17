import unittest

class MonetizationEngine:
    def create_subscription(self, customer_id, plan_id, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if not customer_id or not plan_id:
            raise ValueError("Invalid customer or plan")
        return {"status": "active", "customer_id": customer_id, "plan_id": plan_id, "amount": amount}

class TestRobustMonetization(unittest.TestCase):
    def setUp(self):
        self.engine = MonetizationEngine()

    def test_happy_path_subscription_creation(self):
        res = self.engine.create_subscription("cus_123", "price_pro", 59)
        self.assertEqual(res["status"], "active")
        self.assertEqual(res["amount"], 59)

    def test_edge_case_zero_amount(self):
        with self.assertRaises(ValueError):
            self.engine.create_subscription("cus_123", "price_pro", 0)

    def test_edge_case_negative_pricing(self):
        with self.assertRaises(ValueError):
            self.engine.create_subscription("cus_123", "price_pro", -29)

    def test_error_invalid_customer(self):
        with self.assertRaises(ValueError):
            self.engine.create_subscription("", "price_pro", 59)

if __name__ == '__main__':
    unittest.main()
