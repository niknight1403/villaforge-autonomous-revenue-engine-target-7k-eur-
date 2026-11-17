import unittest
from src.dashboard_metrics import RevenueDashboard

class TestDashboard(unittest.TestCase):
    def test_metrics_update(self):
        db = RevenueDashboard()
        db.update_metrics(7000.0, 0.05, 100)
        self.assertEqual(db.metrics['mrr'], 7000.0)
        self.assertEqual(db.metrics['active_subscriptions'], 100)

if __name__ == '__main__':
    unittest.main()