import unittest
import json
from src.webhook_listener import WebhookListener

class TestStripeWebhookAutomationFinal(unittest.TestCase):
    def setUp(self):
        self.listener = WebhookListener()

    def test_subscription_lifecycle_event(self):
        # Simulate a Stripe subscription.created event
        payload = {
            "type": "customer.subscription.created",
            "data": {
                "object": {
                    "id": "sub_12345",
                    "status": "active",
                    "customer": "cus_abc"
                }
            }
        }
        response = self.listener.handle_event(payload)
        self.assertEqual(response['status'], 'success')
        self.assertIn('processed', response['message'])

    def test_churn_event_detection(self):
        # Simulate a Stripe subscription.deleted event
        payload = {
            "type": "customer.subscription.deleted",
            "data": {
                "object": {
                    "id": "sub_12345",
                    "status": "canceled"
                }
            }
        }
        response = self.listener.handle_event(payload)
        self.assertEqual(response['status'], 'success')
        self.assertIn('churn', response['message'])

if __name__ == '__main__':
    unittest.main()