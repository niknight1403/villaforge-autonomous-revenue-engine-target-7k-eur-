import unittest
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.webhook_listener import StripeWebhookListener
from src.revenue_engine import RevenueEngine

class TestCICDStripeWebhookGate(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=5000)
        self.listener = StripeWebhookListener(self.engine)

    def test_gate_invoice_payment_succeeded(self):
        """Final Quality Gate: Verify invoice.payment_succeeded triggers revenue update."""
        payload = {
            'type': 'invoice.payment_succeeded',
            'data': {'object': {'amount_paid': 5900, 'customer': 'cus_test_123'}}
        }
        response = self.listener.handle(json.dumps(payload))
        self.assertEqual(response.get('status'), 'success')
        self.assertTrue(self.engine.get_mrr() >= 59.00)

    def test_gate_invalid_payload(self):
        """Final Quality Gate: Verify malformed payloads are rejected."""
        response = self.listener.handle("invalid_json")
        self.assertEqual(response.get('status'), 'error')

if __name__ == '__main__':
    unittest.main()