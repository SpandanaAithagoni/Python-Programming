# extract_swift.py
"""
This version does NOT call any real API because the provided domain
(api.swiftshipexpress.in) does not exist.

Instead, it simply loads local sample JSON files stored in:
    data/raw/sample_live.json
    data/raw/sample_traffic.json

This allows the ETL pipeline to run without internet access.
"""

import json
from pathlib import Path


# ----- Folder Setup -----
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def extract_data():
    """
    Instead of fetching API data, this function loads two sample JSON files.

    These files MUST exist:
      - data/raw/sample_live.json
      - data/raw/sample_traffic.json

    Returns:
        (live_file_path, traffic_file_path)
    """
    print("\n--- Extracting SwiftShip Data (Offline Mode) ---")

    live_file = RAW_DIR / "sample_live.json"
    traffic_file = RAW_DIR / "sample_traffic.json"

    # Check if files exist
    if not live_file.exists():
        print("❌ sample_live.json is missing in data/raw/")
        return None, None

    if not traffic_file.exists():
        print("❌ sample_traffic.json is missing in data/raw/")
        return None, None

    print("Using sample files:")
    print("✔ Live deliveries:", live_file)
    print("✔ Route traffic:", traffic_file)

    return str(live_file), str(traffic_file)


# Optional: quick test
if __name__ == "__main__":
    live, traffic = extract_data()
    print("\nExtraction complete.")
    print("Live file loaded:", live)
    print("Traffic file loaded:", traffic)
