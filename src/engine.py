class RevenueEngine:
    def __init__(self):
        self.target_mrr = 7000
        self.plans = {'basic': 50, 'pro': 200, 'enterprise': 1000}
        self.subscriptions = {}

    def update_subscription(self, subscription):
        sub_id = subscription.get('id')
        if sub_id:
            self.subscriptions[sub_id] = subscription
            return True
        return False

    def calculate_mrr(self):
        total = 0
        for sub in self.subscriptions.values():
            plan_price = self.plans.get(sub.get('plan'), 0)
            total += sub.get('users', 0) * plan_price
        return total

    def get_target_gap(self):
        return max(0, self.target_mrr - self.calculate_mrr())

    def suggest_growth_strategy(self):
        gap = self.get_target_gap()
        if gap <= 0:
            return "Target reached. Focus on churn reduction."
        return f"Need {gap} EUR MRR. Focus on upselling existing users or acquiring {int(gap/200) + 1} new Pro users."