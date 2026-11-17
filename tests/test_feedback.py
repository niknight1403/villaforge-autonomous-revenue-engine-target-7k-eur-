import unittest
import os
import json
from src.feedback_collector import FeedbackCollector

class TestFeedbackCollector(unittest.TestCase):
    def setUp(self):
        self.test_file = "data/test_feedback.json"
        self.collector = FeedbackCollector(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_log_feedback(self):
        result = self.collector.log_feedback("user123", "landing_page", 5, "Great service!")
        self.assertTrue(result)
        with open(self.test_file, "r") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["rating"], 5)

if __name__ == "__main__":
    unittest.main()