import requests
import datetime
import pytz
import os

# --- COMMAND HEADER ---
nyc_now = datetime.datetime.now(pytz.timezone('America/New_York'))
header_time = nyc_now.strftime("%d-%m-%Y | %I:%M %p")
print("=" * 60 + f"\n    MANHATTAN AUTO-LOGGER v1.0 | {header_time}\n" + "=" * 60)

# --- THE LOGGING ENGINE ---
def log_session(user, country, rate):
    log_path = os.path.expanduser("~/Desktop/concierge_log.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] USER: {user} | DEST: {country} | RATE: {rate}\n")

# --- NUANCE VAULT ---
vault = {"POLAND": "PLN", "BELARUS": "BYN", "AUSTRIA": "EUR", "ITALY": "EUR", "SPAIN": "EUR"}

try:
    # 1. Fetch live data
    data = requests.get("https://open.er-api.com/v6/latest/USD").json()
    rates = data.get('rates', {})

    # 2. Automated Pulse (No input needed for these)
    print(f"[ HOME PULSE ]")
    print(f"PLN: {rates.get('PLN')} | BYN: {rates.get('BYN')}\n" + "-"*60)

    # 3. The Handshake
    name = input("IDENTIFY YOURSELF: ")
    dest = input("ENTER DESTINATION: ").strip().upper()
    code = vault.get(dest, dest)

    if code in rates:
        live_rate = f"{rates[code]:.2f} {code}"
        print(f"\nSUCCESS: 1 USD = {live_rate}")
        
        # THE UPGRADE: It actually logs now!
        log_session(name, dest, live_rate)
        print(f"SYSTEM: Entry secured to ~/Desktop/concierge_log.txt")
    else:
        print(f"\n[!] ERROR: '{code}' is an invalid bank code.")

except Exception as e:
    print(f"\n[!] CONNECTION FAILED: Check iMac network.")

print("\nSYSTEM STATUS: [STABLE] - PROJECT 01 SECURED. GO TO SLEEP.")