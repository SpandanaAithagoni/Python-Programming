# transform_swift.py
"""
This file transforms raw JSON files into a clean CSV file.

It does 3 things:
1. Load raw live delivery data
2. Load raw traffic data
3. Merge them together using the source city
"""

import json
from pathlib import Path
import pandas as pd
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
STAGED_DIR = BASE_DIR / "data" / "staged"
STAGED_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path: str):
    """Read JSON file and return as Python object."""
    with open(path, "r") as f:
        return json.load(f)


def transform_data(live_file: str, traffic_file: str):
    """Create a clean CSV ready for loading."""
    print("\n--- Transforming Data ---")

    # Load raw data
    live_json = load_json(live_file)
    traffic_json = load_json(traffic_file)

    # Convert shipments list to DataFrame
    deliveries = pd.DataFrame(live_json.get("deliveries", live_json))

    # Convert traffic list to DataFrame
    traffic = pd.DataFrame(traffic_json.get("routes", traffic_json))

    # Rename for clarity
    traffic = traffic.rename(columns={
        "city_name": "source_city",
        "traffic_congestion_score": "congestion",
        "average_speed_on_major_routes": "avg_speed",
        "weather_warnings": "warning"
    })

    # Merge on source city
    merged = deliveries.merge(traffic, on="source_city", how="left")

    # Convert time fields to datetime
    for col in ["dispatch_time", "expected_delivery_time", "actual_delivery_time"]:
        if col in merged.columns:
            merged[col] = pd.to_datetime(merged[col], errors="coerce")

    # Calculate delivery delay (in hours)
    merged["delay_hours"] = (
        merged["actual_delivery_time"] - merged["expected_delivery_time"]
    ).dt.total_seconds() / 3600

    # Classify delay category
    merged["delay_category"] = pd.cut(
        merged["delay_hours"],
        bins=[-999, 0, 2, 5, 20],
        labels=["early_or_on_time", "slightly_delayed", "delayed", "heavily_delayed"]
    )

    # Save staged CSV
    out_path = STAGED_DIR / f"swift_staged_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    merged.to_csv(out_path, index=False)

    print(f"Staged file saved at: {out_path}\n")
    return str(out_path)


if __name__ == "__main__":
    print("Run this through run_pipeline_swift.py")
