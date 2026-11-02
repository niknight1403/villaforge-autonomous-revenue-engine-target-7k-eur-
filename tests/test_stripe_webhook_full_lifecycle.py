import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.revenue_engine import RevenueEngine

class TestStripeWebhookFullLifecycle(unittest.TestCase):
    def setUp(self):
        self.engine = RevenueEngine(target_mrr=5000)

    def test_subscription_churn_and_recovery_flow(self):
        """Validates full lifecycle: creation, churn (past_due), and recovery."""
        events = [
            {"type": "customer.subscription.created", "data": {"object": {"id": "sub_123", "status": "active", "amount": 5900}}},
            {"type": "customer.subscription.updated", "data": {"object": {"id": "sub_123", "status": "past_due"}}},
            {"type": "customer.subscription.updated", "data": {"object": {"id": "sub_123", "status": "active"}}}
        ]
        
        for event in events:
            result = self.engine.process_webhook(event)
            # Handle result if it is a dict or bool
            success = result.get('success') if isinstance(result, dict) else result
            self.assertTrue(success, f"Failed on event {event['type']}")
        
        # Verify engine state
        self.assertEqual(self.engine.get_active_subscriptions(), 1)

if __name__ == '__main__':
    unittest.main()