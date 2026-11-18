import unittest
import os
import json
from src.team_sync import TeamSyncManager

class TestTeamSync(unittest.TestCase):
    def setUp(self):
        self.test_file = "data/test_sync_log.json"
        self.manager = TeamSyncManager(log_file=self.test_file)

    def test_log_sync(self):
        result = self.manager.log_sync(["Agent1", "Agent2"], ["Revenue Goal"], ["None"])
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)

if __name__ == "__main__":
    unittest.main()