import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.revenue_engine import RevenueEngine
from src.webhook_listener import StripeWebhookListener
import json

class TestWebhookListener(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=5000)
        self.listener = StripeWebhookListener(self.engine)

    def test_payment_succeeded_updates_mrr(self):
        payload = {
            'type': 'invoice.payment_succeeded',
            'data': {'object': {'amount_paid': 5900, 'customer': 'cust_123'}}
        }
        result = self.listener.handle(json.dumps(payload))
        self.assertEqual(result['status'], 'success')
        self.assertEqual(self.engine.get_mrr(), 59)

if __name__ == '__main__':
    unittest.main()