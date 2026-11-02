import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.revenue_engine import RevenueEngine

class TestStripeWebhookFullLifecycleValidator(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=5000)

    def test_lifecycle_and_churn_detection(self):
        """Validates full subscription lifecycle and churn detection logic."""
        events = [
            {"type": "customer.subscription.created", "data": {"object": {"id": "sub_123", "status": "active", "plan": {"amount": 5900}}}},
            {"type": "customer.subscription.updated", "data": {"object": {"id": "sub_123", "status": "past_due"}}},
            {"type": "customer.subscription.deleted", "data": {"object": {"id": "sub_123", "status": "canceled"}}}
        ]
        
        for event in events:
            result = self.engine.process_webhook(event)
            self.assertTrue(result if isinstance(result, bool) else result.get('success'), f"Failed to process event: {event['type']}")
        
        # Verify churn state
        status = self.engine.get_subscription_status("sub_123")
        self.assertEqual(status, "canceled", "Subscription should be marked as canceled")

if __name__ == '__main__':
    unittest.main()