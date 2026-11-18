from src.main import calculate_revenue

data = {'tier': 'pro', 'num_users': 10}
result = calculate_revenue(data)
print(f'Revenue for {data}: {result}')