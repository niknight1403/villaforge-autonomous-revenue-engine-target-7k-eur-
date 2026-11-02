import json
import unittest
from unittest.mock import MagicMock

# Mocking the webhook handler logic
def handle_stripe_webhook(event):
    event_type = event.get('type')
    if event_type == 'customer.subscription.created':
        return {'status': 'success', 'action': 'provision_access'}
    elif event_type == 'customer.subscription.deleted':
        return {'status': 'success', 'action': 'revoke_access'}
    return {'status': 'ignored'}

class TestStripeWebhooks(unittest.TestCase):
    def test_subscription_created(self):
        event = {'type': 'customer.subscription.created', 'data': {'id': 'sub_123'}}
        result = handle_stripe_webhook(event)
        self.assertEqual(result['action'], 'provision_access')

    def test_subscription_deleted(self):
        event = {'type': 'customer.subscription.deleted', 'data': {'id': 'sub_123'}}
        result = handle_stripe_webhook(event)
        self.assertEqual(result['action'], 'revoke_access')

if __name__ == '__main__':
    unittest.main()