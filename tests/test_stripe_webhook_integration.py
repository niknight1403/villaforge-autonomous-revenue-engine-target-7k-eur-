import sys
import os
import unittest
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.webhook_listener import StripeWebhookListener
from src.revenue_engine import RevenueEngine

class TestStripeWebhookIntegration(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=5000)
        self.listener = StripeWebhookListener(self.engine)

    def test_subscription_churn_event(self):
        payload = {
            'type': 'customer.subscription.deleted',
            'data': {
                'object': {
                    'id': 'sub_12345',
                    'customer': 'cus_67890',
                    'status': 'canceled'
                }
            }
        }
        result = self.listener.handle(json.dumps(payload))
        self.assertTrue(result is True or (isinstance(result, dict) and result.get('status') == 'success'))
        self.assertIn('event_processed', result)

    def test_subscription_created_event(self):
        payload = {
            'type': 'customer.subscription.created',
            'data': {
                'object': {
                    'id': 'sub_99999',
                    'customer': 'cus_11111',
                    'status': 'active'
                }
            }
        }
        result = self.listener.handle(json.dumps(payload))
        self.assertEqual(result.get('status'), 'success')

if __name__ == '__main__':
    unittest.main()