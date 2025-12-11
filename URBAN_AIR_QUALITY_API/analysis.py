# analysis.py
import os
import pandas as pd
import matplotlib.pyplot as plt
from supabase import create_client
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
TABLE = "air_quality_data"
BASE_DIR = Path(__file__).resolve().parent
PROCESSED_DIR = BASE_DIR / "data/processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Fetch data from Supabase
def fetch_db():
    try:
        res = supabase.table(TABLE).select("*").execute()
        return pd.DataFrame(res.data)
    except Exception:
        return pd.DataFrame()

# MAIN ANALYSIS FUNCTION
def analyze(csv_path):

    print("\n==== ANALYSIS STARTED ====\n")

    df = fetch_db()

    # If Supabase is empty --> fallback to CSV
    if df.empty:
        print("⚠ Supabase table empty. Using staged CSV instead.")
        df = pd.read_csv(csv_path)

    # Ensure time column exists
    if "time" not in df.columns:
        print("❌ ERROR: No 'time' column found — analysis stopped.")
        return

    # Clean timestamp
    df["time"] = pd.to_datetime(df["time"], errors="coerce")
    df = df.dropna(subset=["time"])

    # A. KPI METRICS
    summary = {}

    # 1. City with highest average PM2.5
    summary["highest_pm25_city"] = df.groupby("city")["pm2_5"].mean().idxmax()

    # 2. City with highest severity score
    summary["highest_severity_city"] = df.groupby("city")["severity_score"].mean().idxmax()

    # 3. Worst AQI hour of day
    summary["worst_hour"] = df.groupby(df["time"].dt.hour)["pm2_5"].mean().idxmax()

    # 4. Risk distribution % (high / moderate / low)
    risk_pct = df["risk_level"].value_counts(normalize=True) * 100

    # Save summary
    pd.DataFrame([summary]).to_csv(PROCESSED_DIR / "summary_metrics.csv", index=False)

    # B. City Risk Distribution
    risk_dist = df.groupby(["city", "risk_level"]).size().reset_index(name="count")
    risk_dist.to_csv(PROCESSED_DIR / "city_risk_distribution.csv", index=False)

    # C. Pollution Trends
    trends = df[["city", "time", "pm2_5", "pm10", "ozone"]].sort_values("time")
    trends.to_csv(PROCESSED_DIR / "pollution_trends.csv", index=False)

    # 1. Histogram PM2.5
    plt.hist(df["pm2_5"].dropna(), bins=30)
    plt.title("PM2.5 Distribution")
    plt.xlabel("PM2.5")
    plt.ylabel("Count")
    plt.savefig(PROCESSED_DIR / "pm25_histogram.png")
    plt.close()

    # 2. Bar chart of risk levels per city
    pivot = df.groupby(["city", "risk_level"]).size().unstack(fill_value=0)
    pivot.plot(kind="bar", figsize=(10, 5))
    plt.title("Risk Levels by City")
    plt.ylabel("Count")
    plt.savefig(PROCESSED_DIR / "risk_bar_chart.png")
    plt.close()

    # 3. Line chart — hourly PM2.5 trend
    plt.figure(figsize=(12, 5))
    for city in df["city"].unique():
        sub = df[df["city"] == city]
        plt.plot(sub["time"], sub["pm2_5"], label=city)
    plt.legend()
    plt.title("Hourly PM2.5 Trends")
    plt.xlabel("Time")
    plt.ylabel("PM2.5")
    plt.savefig(PROCESSED_DIR / "pm25_trend.png")
    plt.close()

    # 4. Scatter plot — severity vs PM2.5
    plt.scatter(df["pm2_5"], df["severity_score"], alpha=0.5)
    plt.title("Severity Score vs PM2.5")
    plt.xlabel("PM2.5")
    plt.ylabel("Severity Score")
    plt.savefig(PROCESSED_DIR / "severity_vs_pm25_scatter.png")
    plt.close()

if __name__ == "__main__":
    print("Run analysis only through run_pipeline.py")
