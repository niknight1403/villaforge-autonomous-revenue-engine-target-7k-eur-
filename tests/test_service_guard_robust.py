import unittest
from src.service_guard import ServiceGuard

class TestServiceGuard(unittest.TestCase):
    def setUp(self):
        self.guard = ServiceGuard()

    def test_live_execution_success(self):
        def success_func(): return "live_data"
        result = self.guard.execute(success_func)
        self.assertEqual(result, "live_data")

    def test_fallback_on_failure(self):
        def failing_func(): raise Exception("API Down")
        result = self.guard.execute(failing_func)
        self.assertEqual(result, 5500.0) # get_mrr mock
        self.assertTrue(self.guard.mock_mode)

    def test_reset_guard(self):
        self.guard.mock_mode = True
        self.guard.reset_guard()
        self.assertFalse(self.guard.mock_mode)

if __name__ == '__main__':
    unittest.main()