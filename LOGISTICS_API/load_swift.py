# load_swift.py
"""
Loads staged CSV data into Supabase.
"""

import os
import pandas as pd
from pathlib import Path
from supabase import create_client
from dotenv import load_dotenv
from time import sleep

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

BASE_DIR = Path(__file__).resolve().parent
STAGED_DIR = BASE_DIR / "data" / "staged"


TABLE_NAME = "swift_delivery_data"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS swift_delivery_data (
    id BIGSERIAL PRIMARY KEY,
    shipment_id TEXT,
    source_city TEXT,
    destination_city TEXT,
    dispatch_time TIMESTAMP,
    expected_delivery_time TIMESTAMP,
    actual_delivery_time TIMESTAMP,
    package_weight DOUBLE PRECISION,
    delivery_agent_id TEXT,
    congestion DOUBLE PRECISION,
    avg_speed DOUBLE PRECISION,
    warning TEXT,
    delay_hours DOUBLE PRECISION,
    delay_category TEXT
);
"""


def create_table():
    """Print SQL so user can create the table in Supabase."""
    print("\n--- Create Table SQL ---")
    print(CREATE_TABLE_SQL)
    print("Run this in Supabase SQL editor.\n")


def load_to_supabase(csv_path: str):
    """Load CSV file into Supabase in batches."""
    print("--- Loading to Supabase ---")

    df = pd.read_csv(csv_path)
    df = df.where(pd.notnull(df), None)

    records = df.to_dict(orient="records")
    batch_size = 100
    total = len(records)

    for i in range(0, total, batch_size):
        batch = records[i:i+batch_size]

        try:
            supabase.table(TABLE_NAME).insert(batch).execute()
            print(f"Inserted rows {i+1} to {i+len(batch)}")
        except Exception as e:
            print(f"Error inserting batch {i}: {e}")
            sleep(2)

    print("Load complete.\n")


if __name__ == "__main__":
    print("Run using run_pipeline_swift.py")
