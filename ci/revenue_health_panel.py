import json
import os

def update_revenue_health_panel():
    """Updates the Revenue Health Panel based on test results."""
    report_path = "revenue_health_report.json"
    if not os.path.exists(report_path):
        print("Report not found, initializing RED status.")
        return False

    with open(report_path, "r") as f:
        data = json.load(f)

    # Validate threshold
    if data.get("checks_passed", 0) >= 95:
        print(f"Dashboard Update: Status {data['status']} - Ready for Pilot.")
        return True
    else:
        print(f"Dashboard Update: Status {data['status']} - Pilot Blocked.")
        return False

if __name__ == "__main__":
    if not update_revenue_health_panel():
        exit(1)