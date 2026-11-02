import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.webhook_listener import StripeWebhookListener
from src.revenue_engine import RevenueEngine

class TestStripeWebhookAutomation(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=5000)
        self.listener = StripeWebhookListener(self.engine)

    def test_subscription_lifecycle_validation(self):
        # Simulate lifecycle events
        events = [
            {"type": "customer.subscription.created", "data": {"id": "sub_001", "status": "active"}},
            {"type": "customer.subscription.deleted", "data": {"id": "sub_001", "status": "canceled"}}
        ]
        
        for event in events:
            result = self.listener.handle(str(event).replace("'", '"'))
            self.assertEqual(result.get("status"), "success", f"Failed to process {event['type']}")

    def test_payment_succeeded_mrr_update(self):
        # Simulate payment success event
        event = {
            "type": "invoice.payment_succeeded",
            "data": {"object": {"amount_paid": 5900, "customer": "cus_123"}}
        }
        result = self.listener.handle(str(event).replace("'", '"'))
        self.assertEqual(result.get("status"), "success")
        self.assertIn("mrr", result)

if __name__ == '__main__':
    unittest.main()