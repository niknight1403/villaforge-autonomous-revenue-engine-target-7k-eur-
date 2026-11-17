import os
import subprocess
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_health_check():
    logging.info("Starting automated health check...")
    try:
        # Run existing tests to ensure system integrity
        result = subprocess.run(['python3', '-m', 'unittest', 'discover', 'tests'], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Health check passed: All tests successful.")
            return True
        else:
            logging.error(f"Health check failed: {result.stderr}")
            return False
    except Exception as e:
        logging.error(f"Health check execution error: {str(e)}")
        return False

if __name__ == "__main__":
    run_health_check()