import unittest
from unittest.mock import MagicMock

class MockLLM:
    def generate(self, prompt):
        if "error" in prompt:
            raise Exception("LLM Timeout")
        return "Mocked Response"

class MockStripe:
    def verify_webhook(self, payload, sig):
        if payload == "invalid":
            return False
        return True

class TestMocks(unittest.TestCase):
    def test_llm_success(self):
        llm = MockLLM()
        self.assertEqual(llm.generate("test"), "Mocked Response")

    def test_llm_error(self):
        llm = MockLLM()
        with self.assertRaises(Exception):
            llm.generate("error")

    def test_stripe_success(self):
        stripe = MockStripe()
        self.assertTrue(stripe.verify_webhook("data", "sig"))

if __name__ == '__main__':
    unittest.main()