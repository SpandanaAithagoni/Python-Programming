# transform.py
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
BASE_DIR = Path(__file__).resolve().parent
STAGED_DIR = BASE_DIR / "data/staged"
STAGED_DIR.mkdir(parents=True, exist_ok=True)

# AQI Category Function
def compute_aqi_category(pm25):
    if pd.isna(pm25):
        return "Unknown"
    if pm25 <= 50:
        return "Good"
    if pm25 <= 100:
        return "Moderate"
    if pm25 <= 200:
        return "Unhealthy"
    if pm25 <= 300:
        return "Very Unhealthy"
    return "Hazardous"

# Severity Score Function
def compute_severity(pm25, pm10, no2, so2, co, o3):
    pm25 = pm25 or 0
    pm10 = pm10 or 0
    no2 = no2 or 0
    so2 = so2 or 0
    co = co or 0
    o3 = o3 or 0
    return ((pm25 * 5) + (pm10 * 3) + (no2 * 4) + (so2 * 4) + (co * 2) + (o3 * 3))

# Risk Classification Function
def classify_risk(severity):
    if severity > 400:
        return "High Risk"
    elif severity > 200:
        return "Moderate Risk"
    else:
        return "Low Risk"

# JSON Loader
def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

# Transform Function (Main)
def transform_files(raw_files):
    print("\n==== TRANSFORMING AIR QUALITY DATA ====\n")
    rows = []
    for raw_path in raw_files:
        data = load_json(raw_path)
        
        # Extract city name from filename
        city = Path(raw_path).name.split("_raw_")[0]
        hourly = data.get("hourly", {})
        
        # Extract arrays
        times = hourly.get("time", [])
        pm10 = hourly.get("pm10", [])
        pm25 = hourly.get("pm2_5", [])
        co = hourly.get("carbon_monoxide", [])
        no2 = hourly.get("nitrogen_dioxide", [])
        so2 = hourly.get("sulphur_dioxide", [])
        o3 = hourly.get("ozone", [])
        uv = hourly.get("uv_index", [None] * len(times))  
        
        # Build rows
        for i, t in enumerate(times):
            row = {
                "city": city,
                "time": pd.to_datetime(t),
                "pm10": pm10[i] if i < len(pm10) else None,
                "pm2_5": pm25[i] if i < len(pm25) else None,
                "carbon_monoxide": co[i] if i < len(co) else None,
                "nitrogen_dioxide": no2[i] if i < len(no2) else None,
                "sulphur_dioxide": so2[i] if i < len(so2) else None,
                "ozone": o3[i] if i < len(o3) else None,
                "uv_index": uv[i] if i < len(uv) else None,
            }
            rows.append(row)
            
    # Convert to DataFrame
    df = pd.DataFrame(rows)
    
    # Convert numeric columns
    numeric_cols = ["pm10", "pm2_5", "carbon_monoxide","nitrogen_dioxide", "sulphur_dioxide","ozone", "uv_index"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        
    # Drop rows with ALL pollutants missing
    df.dropna(subset=numeric_cols, how="all", inplace=True)
    
    # Feature Engineering
    df["hour"] = df["time"].dt.hour
    df["aqi_category"] = df["pm2_5"].apply(compute_aqi_category)
    df["severity_score"] = df.apply(
        lambda r: compute_severity(
            r["pm2_5"], r["pm10"], r["nitrogen_dioxide"],
            r["sulphur_dioxide"], r["carbon_monoxide"], r["ozone"]
        ),
        axis=1
    )
    df["risk_level"] = df["severity_score"].apply(classify_risk)
    
    # Save transformed dataset
    out_path = STAGED_DIR / "air_quality_transformed.csv"
    df.to_csv(out_path, index=False)
    print(f"Saved transformed data → {out_path}\n")
    return str(out_path)

# Script Runner
if __name__ == "__main__":
    print("This file is not meant to be run alone. Use run_pipeline.py instead.")
