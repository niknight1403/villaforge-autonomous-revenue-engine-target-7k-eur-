from engine import RevenueEngine

def calculate_revenue(data):
    engine = RevenueEngine()
    return engine.calculate_mrr(data.get('subscriptions', []))

def get_status_report(current_mrr, target=7000):
    engine = RevenueEngine()
    gap = engine.get_target_gap(current_mrr, target)
    return {
        "current_mrr": current_mrr,
        "target_mrr": target,
        "gap": gap,
        "status": "on_track" if gap == 0 else "needs_growth"
    }
