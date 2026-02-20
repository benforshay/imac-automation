import datetime
import os

# Ensures the log file stays inside the 00_master_logger folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def log_session():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = input("Action (IN/OUT/NOTE): ").upper()
    
    entry = f"[{timestamp}] {status}\n"
    
    with open("master_work_log.txt", "a") as f:
        f.write(entry)
    
    print(f"--- Logged: {status} at {timestamp} ---")

if __name__ == "__main__":
    log_session()
