# run_pipeline_swift.py
"""
Runs the full SwiftShip ETL pipeline:

1. Extract
2. Transform
3. Load
4. Analyze
"""

from extract_swift import extract_data
from transform_swift import transform_data
from load_swift import load_to_supabase, create_table
from etl_analysis_swift import analyze


def run_pipeline():
    print("\n========== SwiftShip ETL Started ==========\n")

    # Step 1: Extract
    live_file, traffic_file = extract_data()
    if not live_file or not traffic_file:
        print("Extraction failed. Stopping pipeline.")
        return

    # Step 2: Transform
    staged_csv = transform_data(live_file, traffic_file)

    # Step 3: Load
    create_table()  # User runs SQL manually
    load_to_supabase(staged_csv)

    # Step 4: Analyze
    analyze(staged_csv)

    print("\n========== SwiftShip ETL Completed ==========\n")


if __name__ == "__main__":
    run_pipeline()
