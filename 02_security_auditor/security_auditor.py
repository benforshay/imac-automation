import hashlib
import os
from datetime import datetime

# Path setup
BASE_DIR = os.path.expanduser("~/Developer/imac-automation/02_security_auditor  ")
FILE_TO_WATCH = os.path.join(BASE_DIR, "secure_notes.txt")
HASH_LOG = os.path.join(BASE_DIR, "file_fingerprint.txt")
AUDIT_REPORT = os.path.join(BASE_DIR, "security_audit.log")

def get_fingerprint(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

if not os.path.exists(FILE_TO_WATCH):
    with open(FILE_TO_WATCH, "w") as f:
        f.write("Initial Secure Content")

current_hash = get_fingerprint(FILE_TO_WATCH)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if os.path.exists(HASH_LOG):
    with open(HASH_LOG, "r") as f:
        last_hash = f.read().strip()
    if current_hash == last_hash:
        result = f"[{now}] STATUS: PASS. Integrity intact.\n"
    else:
        result = f"[{now}] WARNING: SECURITY BREACH. File modified!\n"
else:
    result = f"[{now}] INITIALIZED: First fingerprint recorded.\n"

with open(HASH_LOG, "w") as f:
    f.write(current_hash)
with open(AUDIT_REPORT, "a") as f:
    f.write(result)

print(result.strip())