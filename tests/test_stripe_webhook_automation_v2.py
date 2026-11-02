import unittest
import json
from src.webhook_listener import WebhookListener

class TestStripeWebhookAutomation(unittest.TestCase):
    def setUp(self):
        self.listener = WebhookListener()

    def test_subscription_created_event(self):
        payload = {
            "type": "customer.subscription.created",
            "data": {
                "object": {
                    "id": "sub_123",
                    "status": "active",
                    "customer": "cus_123"
                }
            }
        }
        response = self.listener.process_event(payload)
        self.assertTrue(response['success'])

    def test_churn_event(self):
        payload = {
            "type": "customer.subscription.deleted",
            "data": {
                "object": {
                    "id": "sub_123",
                    "status": "canceled"
                }
            }
        }
        response = self.listener.process_event(payload)
        self.assertTrue(response['success'])

if __name__ == '__main__':
    unittest.main()