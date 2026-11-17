import json
import datetime

class RevenueDashboard:
    def __init__(self):
        self.metrics = {
            "mrr": 0.0,
            "churn_rate": 0.0,
            "active_subscriptions": 0,
            "last_updated": str(datetime.datetime.now())
        }

    def update_metrics(self, mrr, churn, subs):
        self.metrics["mrr"] = mrr
        self.metrics["churn_rate"] = churn
        self.metrics["active_subscriptions"] = subs
        self.metrics["last_updated"] = str(datetime.datetime.now())
        with open("metrics_data.json", "w") as f:
            json.dump(self.metrics, f)

    def get_report(self):
        return f"Current MRR: {self.metrics['mrr']} EUR | Active Subs: {self.metrics['active_subscriptions']}"

if __name__ == '__main__':
    dashboard = RevenueDashboard()
    print(dashboard.get_report())