# etl_analysis_swift.py
"""
Simple analysis of SwiftShip delivery data.
"""

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def analyze(csv_path: str):
    print("\n--- Analyzing Data ---")

    df = pd.read_csv(csv_path)

    summary = {
        "total_shipments": len(df),
        "avg_delay_hours": df["delay_hours"].mean(),
        "max_delay": df["delay_hours"].max(),
        "min_delay": df["delay_hours"].min()
    }

    print(summary)

    # Save summary CSV
    summary_path = PROCESSED_DIR / "analysis_summary.csv"
    pd.DataFrame([summary]).to_csv(summary_path, index=False)
    print(f"Saved summary: {summary_path}")

    # Delay histogram
    plt.hist(df["delay_hours"].dropna(), bins=20)
    plt.title("Delivery Delay Distribution")
    plt.xlabel("Delay (hours)")
    plt.ylabel("Count")
    plt.savefig(PROCESSED_DIR / "delay_histogram.png")
    plt.close()

    print("Analysis complete.\n")


if __name__ == "__main__":
    print("Run using run_pipeline_swift.py")
