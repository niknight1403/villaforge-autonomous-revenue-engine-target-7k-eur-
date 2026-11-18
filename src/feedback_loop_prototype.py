import json
import os
from datetime import datetime

class FeedbackLoopPrototype:
    """Automated feedback loop to improve revenue engine messaging."""
    def __init__(self, metrics_path='data/metrics.json'):
        self.metrics_path = metrics_path

    def collect_and_analyze(self, user_engagement_score, conversion_rate):
        feedback = {
            "timestamp": datetime.now().isoformat(),
            "engagement": user_engagement_score,
            "conversion": conversion_rate,
            "action_needed": "optimize_cta" if conversion_rate < 0.05 else "scale_traffic"
        }
        self._save_feedback(feedback)
        return feedback

    def _save_feedback(self, data):
        os.makedirs(os.path.dirname(self.metrics_path), exist_ok=True)
        with open(self.metrics_path, 'w') as f:
            json.dump(data, f)

if __name__ == '__main__':
    loop = FeedbackLoopPrototype()
    result = loop.collect_and_analyze(0.85, 0.04)
    print(f"Feedback loop processed: {result}")