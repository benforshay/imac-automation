import os
import time
from datetime import datetime

# Path setup for the Backup Check
# We are checking the main automation folder to see if it's "stale"
TARGET_FOLDER = os.path.expanduser("~/Developer/imac-automation")
BASE_DIR = os.path.expanduser("~/Developer/imac-automation/04_backup_check")
LOG_FILE = os.path.join(BASE_DIR, "backup_integrity.log")

def verify_backup():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_size = 0
    latest_mod = 0

    # Walk through the folder to find the newest file and total size
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for f in files:
            fp = os.path.join(root, f)
            total_size += os.path.getsize(fp)
            mtime = os.path.getmtime(fp)
            if mtime > latest_mod:
                latest_mod = mtime

    # Calculate days since last edit
    days_since_edit = round((time.time() - latest_mod) / (24 * 3600), 2)
    size_mb = round(total_size / (1024 * 1024), 2)

    status = f"[{now}] VERIFY: {size_mb} MB total. Last edit: {days_since_edit} days ago.\n"
    
    if days_since_edit > 7:
        status += f"[{now}] WARNING: Stale data! No changes in over a week.\n"

    # Log it and Print it (Indented so it stays inside the function)
    with open(LOG_FILE, "a") as f:
        f.write(status)
    print(status.strip()) # This will now see 'status' and print it!

if __name__ == "__main__":
    verify_backup()