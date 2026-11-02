import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.webhook_listener import StripeWebhookListener
from src.revenue_engine import RevenueEngine

class TestStripeWebhookSimulatorFinal(unittest.TestCase):
    def setUp(self):
        # Initialize engine with target MRR as required by constructor
        self.engine = RevenueEngine(target_mrr=5000)
        self.listener = StripeWebhookListener(self.engine)

    def test_webhook_event_processing(self):
        # Simulate a Stripe invoice.payment_succeeded event
        event = {
            'type': 'invoice.payment_succeeded',
            'data': {'object': {'amount_paid': 5900, 'customer': 'cus_123'}}
        }
        import json
        result = self.listener.handle(json.dumps(event))
        self.assertEqual(result.get('status'), 'success')

    def test_invalid_event_handling(self):
        # Simulate unknown event
        event = {'type': 'unknown.event'}
        import json
        result = self.listener.handle(json.dumps(event))
        # Verify failure handling for unknown events
        self.assertNotEqual(result.get('status'), 'success')

if __name__ == '__main__':
    unittest.main()