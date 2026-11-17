import pytest
from unittest.mock import MagicMock

class MockLLM:
    def generate(self, prompt):
        return "{\"status\": \"success\", \"data\": \"mocked_response\"}"

class MockStripe:
    def verify_webhook(self, payload, sig_header):
        return {"id": "evt_123", "type": "invoice.payment_succeeded"}

@pytest.fixture
def mock_llm():
    return MockLLM()

@pytest.fixture
def mock_stripe():
    return MockStripe()
