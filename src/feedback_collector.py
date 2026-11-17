import json
import os
from datetime import datetime

class FeedbackCollector:
    def __init__(self, storage_path="data/feedback.json"):
        self.storage_path = storage_path
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)

    def log_feedback(self, user_id, page_type, rating, comment):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "page_type": page_type,
            "rating": rating,
            "comment": comment
        }
        data = []
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        
        data.append(entry)
        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=4)
        return True

if __name__ == "__main__":
    collector = FeedbackCollector()
    print("Feedback system initialized.")