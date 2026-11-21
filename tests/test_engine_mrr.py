from src.engine import RevenueEngine

def test_mrr_calculation():
    engine = RevenueEngine()
    # Test with 10 pro users (200 each = 2000)
    data = [{'plan': 'pro', 'users': 10}]
    mrr = engine.calculate_mrr(data)
    assert mrr == 2000, f'Expected 2000, got {mrr}'
    print('Test Passed: MRR calculation is correct.')

if __name__ == '__main__':
    test_mrr_calculation()