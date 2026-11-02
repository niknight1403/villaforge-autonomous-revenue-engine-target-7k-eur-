import unittest
from src.webhook_listener import WebhookListener

class TestStripeWebhookAutomation(unittest.TestCase):
    def setUp(self):
        self.listener = WebhookListener()

    def test_full_subscription_lifecycle(self):
        # Simulate Stripe Webhook Events
        events = [
            {'type': 'customer.subscription.created', 'data': {'id': 'sub_123'}},
            {'type': 'invoice.payment_succeeded', 'data': {'subscription': 'sub_123'}},
            {'type': 'customer.subscription.deleted', 'data': {'id': 'sub_123'}}
        ]

        for event in events:
            # Process event and ensure return is a dict with 'success' key
            result = self.listener.handle_event(event)
            self.assertIsInstance(result, dict, f"Result should be a dict for {event['type']}")
            self.assertTrue(result.get('success'), f"Failed to process {event['type']}: {result.get('error')}")

if __name__ == '__main__':
    unittest.main()