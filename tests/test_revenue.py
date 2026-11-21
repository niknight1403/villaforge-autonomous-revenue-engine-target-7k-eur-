import sys
import os

# Add src to path
sys.path.append(os.path.abspath('src'))
from main import calculate_revenue

def test_calculate_revenue():
    data = {'subscriptions': [{'plan': 'pro', 'users': 10}]}
    result = calculate_revenue(data)
    assert result == 2000, f'Expected 2000, got {result}'
    print('Test passed!')

if __name__ == '__main__':
    test_calculate_revenue()