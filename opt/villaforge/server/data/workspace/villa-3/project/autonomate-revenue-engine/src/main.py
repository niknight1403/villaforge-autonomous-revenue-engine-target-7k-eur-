def calculate_revenue(data):
    plans = {
        'basic': 50,
        'pro': 200,
        'enterprise': 1000
    }
    total = 0
    for sub in data.get('subscriptions', []):
        plan_price = plans.get(sub['plan'], 0)
        total += sub['users'] * plan_price
    return total