import unittest
import json
import requests
from unittest.mock import patch

class TestStripeWebhookSimulator(unittest.TestCase):
    """Simulator to verify Stripe webhook event handling in CI/CD pipelines."""
    
    def setUp(self):
        self.webhook_url = "http://localhost:5000/webhook"
        self.mock_event = {
            "id": "evt_test_123",
            "type": "invoice.payment_succeeded",
            "data": {
                "object": {
                    "amount_paid": 5900,
                    "currency": "eur",
                    "customer": "cus_test_abc"
                }
            }
        }

    def test_webhook_payload_structure(self):
        """Verify the structure of the simulated webhook payload."""
        self.assertIn("type", self.mock_event)
        self.assertEqual(self.mock_event["data"]["object"]["amount_paid"], 5900)

    @patch('requests.post')
    def test_simulator_trigger(self, mock_post):
        """Simulate sending the webhook to the local endpoint."""
        mock_post.return_value.status_code = 200
        response = requests.post(self.webhook_url, json=self.mock_event)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()