import unittest
import json
from src.webhook_listener import WebhookListener

class TestStripeWebhookSimulatorFinal(unittest.TestCase):
    def setUp(self):
        self.listener = WebhookListener()
        self.simulator_payload = {
            "id": "evt_test_123",
            "type": "invoice.payment_succeeded",
            "data": {
                "object": {
                    "amount_paid": 5900,
                    "currency": "eur",
                    "customer": "cus_test_999"
                }
            }
        }

    def test_webhook_simulation_flow(self):
        """Verifies that the simulator payload triggers the listener correctly."""
        response = self.listener.process_event(self.simulator_payload)
        self.assertEqual(response, 200, "Simulator failed to trigger 200 OK from listener")

    def test_invalid_payload_handling(self):
        """Verifies that malformed payloads are rejected by the gate."""
        invalid_payload = {"error": "malformed"}
        response = self.listener.process_event(invalid_payload)
        self.assertNotEqual(response, 200, "Listener accepted invalid payload")

if __name__ == '__main__':
    unittest.main()