import unittest
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.webhook_listener import StripeWebhookListener as WebhookListener

class TestStripeWebhookValidatorSuite(unittest.TestCase):
    def setUp(self):
        from src.revenue_engine import RevenueEngine
        self.engine = RevenueEngine(target_mrr=5000)
        self.listener = WebhookListener(self.engine)

    def test_subscription_created_event(self):
        payload = {
            "type": "customer.subscription.created",
            "data": {
                "object": {
                    "id": "sub_123",
                    "status": "active",
                    "plan": {"amount": 5900, "currency": "eur"}
                }
            }
        }
        result = self.listener.handle(json.dumps(payload))
        self.assertTrue(result['success'])
        self.assertEqual(result['mrr_impact'], 59.0)

    def test_subscription_deleted_event(self):
        payload = {
            "type": "customer.subscription.deleted",
            "data": {
                "object": {
                    "id": "sub_123",
                    "status": "canceled"
                }
            }
        }
        result = self.listener.handle(json.dumps(payload))
        self.assertTrue(result['success'])
        self.assertEqual(result['mrr_impact'], -59.0)

if __name__ == '__main__':
    unittest.main()