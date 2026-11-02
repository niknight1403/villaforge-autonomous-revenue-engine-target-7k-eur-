import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.revenue_engine import RevenueEngine

class TestStripeWebhookLifecycleValidator(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=5000)

    def test_churn_analysis_trigger(self):
        """Validates that a 'canceled' status triggers churn logic in the engine."""
        event = {
            "type": "customer.subscription.deleted",
            "data": {
                "object": {
                    "id": "sub_test_123",
                    "status": "canceled",
                    "customer": "cus_123"
                }
            }
        }
        result = self.engine.process_webhook(event)
        self.assertTrue(result if isinstance(result, bool) else result.get('success'), "Engine failed to process cancellation event")
        self.assertIn('churn_detected', result.get('metadata', {}), "Churn analysis not triggered")

    def test_mrr_update_on_active(self):
        """Validates that an 'active' status updates the MRR metrics."""
        event = {
            "type": "customer.subscription.created",
            "data": {
                "object": {
                    "id": "sub_test_456",
                    "status": "active",
                    "plan": {"amount": 5900}
                }
            }
        }
        result = self.engine.process_webhook(event)
        self.assertTrue(result if isinstance(result, bool) else result.get('success'), "Engine failed to process active subscription")
        self.assertEqual(result.get('mrr'), 5900, "MRR delta mismatch") if isinstance(result, dict) else self.fail("Result is not a dict")

if __name__ == '__main__':
    unittest.main()