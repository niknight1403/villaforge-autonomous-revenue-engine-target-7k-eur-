import unittest
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.webhook_listener import StripeWebhookListener as WebhookListener

class TestStripeWebhookFinalValidator(unittest.TestCase):
    def setUp(self):
        from src.revenue_engine import RevenueEngine
        self.engine = RevenueEngine(target_mrr=7000.0)
        self.listener = WebhookListener(self.engine)

    def test_webhook_event_processing(self):
        """Simulates a production-ready Stripe webhook event for CI/CD validation."""
        mock_event = {
            "type": "invoice.payment_succeeded",
            "data": {
                "object": {
                    "amount_paid": 5900,
                    "currency": "eur",
                    "customer": "cus_12345"
                }
            }
        }
        result = self.listener.process_event(mock_event)
        self.assertTrue(result, "Webhook listener failed to process valid invoice event")

    def test_invalid_event_rejection(self):
        """Ensures the system rejects malformed events."""
        mock_event = {"type": "invalid.event"}
        result = self.listener.process_event(mock_event)
        self.assertFalse(result, "Webhook listener should reject invalid event types")

if __name__ == '__main__':
    unittest.main()