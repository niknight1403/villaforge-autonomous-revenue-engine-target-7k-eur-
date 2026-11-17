import os
import json
import logging
from datetime import datetime

# Sicherstellen, dass Verzeichnisse existieren
os.makedirs('logs', exist_ok=True)
os.makedirs('data', exist_ok=True)

LOG_FILE = "logs/system_monitor.log"
METRICS_FILE = "data/metrics.json"

logging.basicConfig(level=logging.INFO, filename=LOG_FILE, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_metric(key, value):
    data = {}
    if os.path.exists(METRICS_FILE):
        with open(METRICS_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    
    data[key] = value
    data['last_updated'] = datetime.now().isoformat()
    
    with open(METRICS_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    logging.info(f"Metric updated: {key} = {value}")

if __name__ == '__main__':
    log_metric('status', 'operational')
    print('Feedback loop initialized successfully.')