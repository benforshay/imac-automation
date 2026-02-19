import os
import hashlib
from datetime import datetime

# --- CONFIGURATION (Dynamic Path Setup) ---
# This looks at the folder where this script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# These lines join that folder path with your filenames
FILE_TO_WATCH = os.path.join(BASE_DIR, "secure_notes.txt")
FINGERPRINT_FILE = os.path.join(BASE_DIR, "file_fingerprint.txt")
LOG_FILE = os.path.join(BASE_DIR, "security_audit.log")

def get_file_hash(filepath):
    """Generates a SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def run_audit():
    """Runs the integrity check and logs the result."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not os.path.exists(FILE_TO_WATCH):
        print(f"[{timestamp}] ERROR: {FILE_TO_WATCH} not found.")
        return

    current_hash = get_file_hash(FILE_TO_WATCH)

    # If fingerprint doesn't exist, create it (First run)
    if not os.path.exists(FINGERPRINT_FILE):
        with open(FINGERPRINT_FILE, "w") as f:
            f.write(current_hash)
        result = f"[{timestamp}] INITIALIZED: New fingerprint created."
    else:
        with open(FINGERPRINT_FILE, "r") as f:
            stored_hash = f.read().strip()
        
        if current_hash == stored_hash:
            result = f"[{timestamp}] VERIFY: {os.path.basename(FILE_TO_WATCH)} integrity confirmed."
        else:
            result = f"[{timestamp}] ALERT: {os.path.basename(FILE_TO_WATCH)} has been modified!"

    print(result)
    with open(LOG_FILE, "a") as log:
        log.write(result + "\n")

if __name__ == "__main__":
    run_audit() 