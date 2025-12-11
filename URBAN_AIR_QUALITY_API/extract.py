# extract.py
import os
import json
import time
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Load retry settings
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
TIMEOUT = int(os.getenv("TIMEOUT", 15))
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / os.getenv("RAW_DIR", "data/raw")
LOG_DIR = BASE_DIR / "data/logs"
RAW_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
ERROR_LOG = LOG_DIR / "extract_errors.log"
# Cities and coordinates
CITIES = {
    "Delhi": (28.7041, 77.1025),
    "Bangalore": (12.9716, 77.5946),
    "Hyderabad": (17.3850, 78.4867),
    "Mumbai": (19.0760, 72.8777),
    "Kolkata": (22.5726, 88.3639)
}

def log_error(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERROR_LOG, "a") as f:
        f.write(f"{ts} - {msg}\n")

def save_json(data, city):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = RAW_DIR / f"{city.lower()}_raw_{ts}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved → {path}")
    return str(path)

def fetch_with_retry(url, desc):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"{desc} (Attempt {attempt})...")
            res = requests.get(url, timeout=TIMEOUT)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            print(f"Error: {e}")
            log_error(f"{desc} attempt {attempt}: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(2)
    return None

def extract_all():
    print("\n==== AIR QUALITY EXTRACTION STARTED ====\n")
    saved_files = []
    for city, (lat, lon) in CITIES.items():
        print(f"\n--- Fetching data for {city} ---")
        url = (
            f"https://air-quality-api.open-meteo.com/v1/air-quality"
            f"?latitude={lat}&longitude={lon}"
            "&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,ozone,sulphur_dioxide"
        )
        data = fetch_with_retry(url, f"Fetching {city}")
        if data:
            saved_files.append(save_json(data, city))
        else:
            print(f"⚠ No data for {city}")
    print("\nExtraction complete.\n")
    return saved_files

if __name__ == "__main__":
    extract_all()