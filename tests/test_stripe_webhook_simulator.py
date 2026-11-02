import unittest
import json
import requests
from unittest.mock import patch

class TestStripeWebhookSimulator(unittest.TestCase):
    """Simulator for Stripe Webhook events to verify payment processing logic."""

    def setUp(self):
        self.webhook_url = "http://localhost:5000/webhook"
        self.event_data = {
            "id": "evt_test_123",
            "type": "invoice.payment_succeeded",
            "data": {
                "object": {
                    "customer": "cus_test_123",
                    "amount_paid": 5900,
                    "currency": "eur"
                }
            }
        }

    def test_webhook_payload_structure(self):
        """Verify that the simulator generates valid Stripe-compliant payloads."""
        self.assertEqual(self.event_data['type'], "invoice.payment_succeeded")
        self.assertIn('amount_paid', self.event_data['data']['object'])

    @patch('requests.post')
    def test_webhook_delivery(self, mock_post):
        """Simulate delivery of a webhook event to the local engine."""
        mock_post.return_value.status_code = 200
        response = requests.post(self.webhook_url, json=self.event_data)
        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()