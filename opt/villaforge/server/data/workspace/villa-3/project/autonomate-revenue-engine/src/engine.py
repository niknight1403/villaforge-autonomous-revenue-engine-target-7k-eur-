class RevenueEngine:
    def __init__(self):
        self.plans = {'basic': 50, 'pro': 200, 'enterprise': 1000}

    def calculate_mrr(self, subscriptions):
        total = 0
        for sub in subscriptions:
            plan_price = self.plans.get(sub.get('plan'), 0)
            total += sub.get('users', 0) * plan_price
        return total

    def get_target_gap(self, current_mrr, target=7000):
        return max(0, target - current_mrr)