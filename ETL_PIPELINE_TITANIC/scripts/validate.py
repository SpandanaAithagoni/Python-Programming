# validate.py
# Purpose: Validate transformed Titanic dataset and Supabase-loaded table

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
    print("Running Titanic data validation...\n")

    # Load transformed CSV
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "staged", "titanic_transformed.csv")

    if not os.path.exists(csv_path):
        print(f"CSV file not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    csv_rows = len(df)
    print(f"CSV rows: {csv_rows}")

    # Load Supabase table
    try:
        supabase = get_supabase_client()
        response = supabase.table("titanic_data").select("*").execute()

        if hasattr(response, "data"):
            sb_df = pd.DataFrame(response.data)
        else:
            sb_df = pd.DataFrame(response.get("data", []))

        sb_rows = len(sb_df)
        print(f"Supabase rows: {sb_rows}")

    except Exception as e:
        print(f"Error loading Supabase data: {e}")
        return

    print("\nValidation Results")
    print("----------------------")

    # Missing value check
    required_columns = ["survived", "pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"]
    print("\nMissing values:")
    for col in required_columns:
        if col not in df.columns:
            print(f"{col}: column not found")
        else:
            missing = df[col].isna().sum()
            print(f"{col}: {missing} missing")

    # Row count match
    print("\nRow count match:")
    print(f"CSV rows: {csv_rows}")
    print(f"Supabase rows: {sb_rows}")
    if csv_rows == sb_rows:
        print("Row count matches")
    else:
        print("Row count does NOT match")

    # Duplicate row check
    unique_rows = len(df.drop_duplicates())
    print("\nDuplicate rows:")
    if unique_rows == csv_rows:
        print("No duplicates")
    else:
        print(f"Duplicates found: {csv_rows - unique_rows}")

    # Simple categorical value checks
    print("\nCategorical values:")
    if "sex" in df:
        print(f"sex values: {set(df['sex'].unique())}")

    if "embarked" in df:
        print(f"embarked values: {set(df['embarked'].unique())}")

    if "title" in df:
        missing_titles = df["title"].isna().sum()
        print(f"title missing values: {missing_titles}")

    # Boolean columns
    print("\nBoolean columns check:")
    if "alone" in df:
        print(f"alone valid: {df['alone'].dropna().isin([True, False]).all()}")

    if "is_alone" in df:
        print(f"is_alone valid: {df['is_alone'].dropna().isin([0, 1]).all()}")

    print("\nValidation complete.")


if __name__ == "__main__":
    validate_data()
