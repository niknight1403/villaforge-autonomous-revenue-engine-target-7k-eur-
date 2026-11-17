import json
import os
from datetime import datetime

class FeedbackAnalyzer:
    """
    Analysiert Feedback-Daten zur MRR-Optimierung.
    """
    def __init__(self, feedback_file='data/feedback.json'):
        self.feedback_file = feedback_file

    def analyze_mrr_potential(self):
        if not os.path.exists(self.feedback_file):
            return {"status": "no_data", "action": "collect_feedback"}
        
        with open(self.feedback_file, 'r') as f:
            data = json.load(f)
        
        # Logik zur Identifikation von Churn-Risiken oder Up-Sell Potentialen
        insights = []
        for entry in data:
            if entry.get('sentiment') == 'negative' and entry.get('category') == 'pricing':
                insights.append({"action": "adjust_pricing_tier", "reason": entry.get('comment')})
            elif entry.get('sentiment') == 'positive' and entry.get('feature_request'):
                insights.append({"action": "prioritize_feature", "feature": entry.get('feature_request')})
        
        return {"timestamp": str(datetime.now()), "insights": insights}

if __name__ == "__main__":
    analyzer = FeedbackAnalyzer()
    print(json.dumps(analyzer.analyze_mrr_potential(), indent=2))