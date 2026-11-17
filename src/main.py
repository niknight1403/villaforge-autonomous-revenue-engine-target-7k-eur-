def calculate_revenue(data):
    tier_prices = {
        'basic': 50,
        'pro': 200,
        'enterprise': 500
    }
    tier = data.get('tier', 'basic')
    num_users = data.get('num_users', 1)
    return tier_prices.get(tier, 50) * num_users