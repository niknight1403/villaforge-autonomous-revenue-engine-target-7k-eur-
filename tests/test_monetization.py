import pytest
from src.monetization import calculate_mrr

def test_calculate_mrr_basic():
    # Test with 10 users at 50 EUR each
    users = 10
    price = 50
    expected = 500
    assert calculate_mrr(users, price) == expected

def test_calculate_mrr_zero():
    # Test with 0 users
    assert calculate_mrr(0, 100) == 0

def test_calculate_mrr_negative_input():
    # Test resilience against negative inputs
    with pytest.raises(ValueError):
        calculate_mrr(-1, 100)

def test_calculate_mrr_float_price():
    # Test with float price
    assert calculate_mrr(2, 49.99) == 99.98
