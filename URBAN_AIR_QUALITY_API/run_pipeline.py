# run_pipeline.py
from extract import extract_all
from transform import transform_files
from load import load_to_supabase
from analysis import analyze

def run_pipeline():
    print("\n--- AIR QUALITY ETL STARTED ---\n")
    raw_files = extract_all()
    if not raw_files:
        print("No raw files extracted. Stopping pipeline.")
        return
    transformed_csv = transform_files(raw_files)
    load_to_supabase(transformed_csv)
    analyze(transformed_csv)
    print("\n--- AIR QUALITY ETL COMPLETED ---\n")

if __name__ == "__main__":
    run_pipeline()
