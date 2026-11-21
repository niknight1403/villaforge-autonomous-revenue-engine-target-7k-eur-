from src.engine import RevenueEngine

def test_engine():
    engine = RevenueEngine()
    gap = engine.get_target_gap(0)
    print(f'Engine initialized. Target gap for 0 MRR: {gap}')
    assert gap == 7000
    print('Verification successful.')

if __name__ == '__main__':
    test_engine()