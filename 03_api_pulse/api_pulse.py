import requests
import os
from datetime import datetime
import time

# Path setup - points to our new dedicated folder
BASE_DIR = os.path.expanduser("~/Developer/imac-automation/03_api_pulse")
HEALTH_LOG = os.path.join(BASE_DIR, "network_health.log")

# We'll check Google to verify the iMac's outside connection
TARGET = "https://www.google.com"

def check_network():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        start = time.time()
        # Sending a 'GET' request to the web
        response = requests.get(TARGET, timeout=5)
        # Calculate how many milliseconds it took to respond
        latency = round((time.time() - start) * 1000)
        
        if response.status_code == 200:
            result = f"[{now}] PULSE OK: {latency}ms response time.\n"
        else:
            result = f"[{now}] PULSE WEAK: Status Code {response.status_code}\n"
            
    except Exception as e:
        result = f"[{now}] PULSE LOST: Connection Error - {e}\n"

    # Save to our new log file
    with open(HEALTH_LOG, "a") as f:
        f.write(result)
    print(result.strip())

if __name__ == "__main__":
    check_network()