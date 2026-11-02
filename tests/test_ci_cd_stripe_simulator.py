import unittest
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.webhook_listener import StripeWebhookListener
from src.revenue_engine import RevenueEngine

class TestCICDStripeSimulator(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=5000)
        self.listener = StripeWebhookListener(self.engine)

    def test_ci_cd_webhook_gate(self):
        """Finales CI/CD-Qualitätstor: Simuliert Stripe-Events und validiert Revenue-Logik."""
        events = [
            {"type": "invoice.payment_succeeded", "data": {"object": {"customer": "cus_test_1", "amount_paid": 5900, "currency": "eur"}}},
            {"type": "customer.subscription.deleted", "data": {"object": {"customer": "cus_test_1"}}}
        ]
        
        for event in events:
            response = self.listener.process_event(event)
            self.assertEqual(response['status'], 'success', f"Event {event['type']} failed validation")

if __name__ == '__main__':
    unittest.main()