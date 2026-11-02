import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from revenue_engine import RevenueEngine

class TestRevenueEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=6000)

    def test_initial_state(self):
        self.assertEqual(self.engine.target_mrr, 6000)
        self.assertEqual(len(self.engine.customers), 0)

    def test_add_customer_valid(self):
        cust = self.engine.add_customer("Acme Corp", 59)
        self.assertTrue(cust['active'])
        self.assertEqual(self.engine.get_mrr(), 59)

    def test_add_customer_edge_zero_amount(self):
        with self.assertRaises(ValueError):
            self.engine.add_customer("ZeroPay", 0)

    def test_add_customer_edge_negative_amount(self):
        with self.assertRaises(ValueError):
            self.engine.add_customer("MinusPay", -10)

    def test_remove_customer(self):
        cust = self.engine.add_customer("StartupX", 49)
        self.assertEqual(self.engine.get_mrr(), 49)
        self.engine.remove_customer(cust['id'])
        self.assertEqual(self.engine.get_mrr(), 0)

    def test_remove_nonexistent_customer(self):
        result = self.engine.remove_customer("nonexistent-id")
        self.assertFalse(result)

    def test_mrr_calculation_multiple(self):
        self.engine.add_customer("C1", 29)
        self.engine.add_customer("C2", 59)
        self.engine.add_customer("C3", 149)
        self.assertEqual(self.engine.get_mrr(), 237)

    def test_forecast_revenue(self):
        self.engine.add_customer("C1", 100)
        forecast = self.engine.forecast_revenue(months=3)
        self.assertEqual(forecast, 300)

    def test_forecast_invalid_months(self):
        with self.assertRaises(ValueError):
            self.engine.forecast_revenue(months=-1)

    def test_churn_rate_calculation(self):
        self.engine.add_customer("C1", 100)
        self.engine.remove_customer("c1")
        self.assertEqual(self.engine.get_mrr(), 0)