import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from optimization import RevenueOptimizer

def test_smoke():
    optimizer = RevenueOptimizer()
    mrr = optimizer.calculate_mrr(100, 49)
    assert mrr == 4900, f"Expected 4900, got {mrr}"
    print("Smoke test passed successfully!")

if __name__ == "__main__":
    try:
        test_smoke()
        sys.exit(0)
    except Exception as e:
        print(f"Smoke test failed: {e}", file=sys.stderr)
        sys.exit(1)
