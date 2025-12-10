# validate.py
# Purpose: Validate transformed churn dataset and Supabase-loaded table

import os
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv


def get_supabase_client():
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY in .env")

    return create_client(url, key)


def validate_data():
    print("Running churn validation...\n")

    # Load CSV
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "staged", "churn_transformed.csv")

    if not os.path.exists(csv_path):
        print(f"CSV file not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    csv_rows = len(df)
    print(f"CSV rows: {csv_rows}")

    # Load Supabase data
    try:
        supabase = get_supabase_client()
        response = supabase.table("churn_data").select("*").execute()

        if hasattr(response, "data"):
            sb_df = pd.DataFrame(response.data)
        else:
            sb_df = pd.DataFrame(response.get("data", []))

        sb_rows = len(sb_df)
        print(f"Supabase rows: {sb_rows}")

    except Exception as e:
        print(f"Error reading Supabase data: {e}")
        return

    print("\nValidation Results")
    print("------------------------------")

    # 1. Missing value checks
    required_columns = ["tenure", "MonthlyCharges", "TotalCharges"]
    print("\nMissing values:")
    for col in required_columns:
        missing = df[col].isna().sum()
        print(f"{col}: {missing} missing")

    # 2. Row count match
    print("\nRow count match:")
    print(f"CSV rows: {csv_rows}")
    print(f"Supabase rows: {sb_rows}")
    if csv_rows == sb_rows:
        print("Row count matches")
    else:
        print("Row count does not match")

    # 3. Duplicate row check
    unique_rows = len(df.drop_duplicates())
    print("\nDuplicate rows:")
    if unique_rows == csv_rows:
        print("No duplicates")
    else:
        print(f"Duplicates found: {csv_rows - unique_rows}")

    # 4. Tenure group validation
    expected_tenure_groups = {"New", "Regular", "Loyal", "Champion"}
    actual_tenure_groups = set(df["tenure_group"].unique())
    print("\nTenure groups present:", actual_tenure_groups)
    missing_tenure = expected_tenure_groups - actual_tenure_groups
    if missing_tenure:
        print("Missing tenure groups:", missing_tenure)

    # 5. Monthly charge segment validation
    expected_segments = {"Low", "Medium", "High"}
    actual_segments = set(df["monthly_charge_segment"].unique())
    print("\nMonthly charge segments present:", actual_segments)
    missing_segments = expected_segments - actual_segments
    if missing_segments:
        print("Missing monthly charge segments:", missing_segments)

    # 6. Contract code validation
    valid_codes = {0, 1, 2}
    actual_codes = set(df["contract_type_code"].unique())
    print("\nContract type codes:", actual_codes)
    invalid_codes = actual_codes - valid_codes
    if invalid_codes:
        print("Invalid contract codes:", invalid_codes)
    else:
        print("Contract codes valid")

    print("\nValidation complete.")


if __name__ == "__main__":
    validate_data()
