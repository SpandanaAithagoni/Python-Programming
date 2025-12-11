# load.py
import os
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv
from time import sleep
import numpy as np
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
TABLE = "air_quality_data"

def clean_value(v):
    """Supabase does NOT allow NaN, Infinity"""
    if v is None:
        return None
    if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
        return None
    return v

def load_to_supabase(csv_path, batch_size=200):
    print("\n==== LOADING INTO SUPABASE ====\n")
    df = pd.read_csv(csv_path)

    # Clean datetime
    df["time"] = pd.to_datetime(df["time"], errors="coerce")
    df = df[df["time"].notna()]   # remove invalid rows
    df["time"] = df["time"].astype(str)

    # Clean numeric fields
    df = df.applymap(clean_value)

    # Convert dataframe to dict
    records = df.to_dict(orient="records")
    total = len(records)
    print(f"Total rows to upload: {total}")
    batch_no = 0

    # Batch insert
    for i in range(0, total, batch_size):
        batch = records[i:i + batch_size]
        batch_no += 1
        for attempt in range(1, 3):
            try:
                supabase.table(TABLE).insert(batch).execute()
                print(f"✔ Batch {batch_no} uploaded ({i+1} → {i+len(batch)})")
                break
            except Exception as e:
                print(f"⚠ Batch {batch_no} failed (Attempt {attempt}): {e}")
                sleep(2)
    print("\n==== SUPABASE LOAD COMPLETE ====\n")
