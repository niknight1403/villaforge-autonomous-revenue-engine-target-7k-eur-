import unittest
from service_guard import ServiceGuard

class TestServiceGuard(unittest.TestCase):
    def test_service_is_running(self):
        guard = ServiceGuard()
        self.assertTrue(guard.is_running())

if __name__ == '__main__':
    unittest.main()