import random
import json
import os

class ABTestManager:
    def __init__(self, config_path='data/ab_config.json'):
        self.config_path = config_path
        self.variants = ['A', 'B']

    def get_variant(self, user_id):
        # Deterministic assignment based on user_id
        return self.variants[hash(str(user_id)) % len(self.variants)]

    def record_conversion(self, variant, converted=True):
        data = self._load_data()
        data[variant]['conversions'] += 1 if converted else 0
        data[variant]['views'] += 1
        with open(self.config_path, 'w') as f:
            json.dump(data, f)

    def _load_data(self):
        if not os.path.exists(self.config_path):
            return {'A': {'views': 0, 'conversions': 0}, 'B': {'views': 0, 'conversions': 0}}
        with open(self.config_path, 'r') as f:
            return json.load(f)

if __name__ == '__main__':
    manager = ABTestManager()
    print(f'Assigned Variant: {manager.get_variant("test_user_123")}')