import os
import pandas as pd

# Purpose: Clean and transform Telco Customer Churn dataset
def transform_data(raw_path):

    # Ensure the path is relative to project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    staged_dir = os.path.join(base_dir, "data", "staged")
    os.makedirs(staged_dir, exist_ok=True)

    # Load raw data
    df = pd.read_csv(raw_path)

    # 1️⃣ CLEANING TASKS

    # Convert TotalCharges → numeric (handles blank spaces becoming NaN)
    if "TotalCharges" in df:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Fill missing numeric values
    numeric_fill_map = {
        "tenure": df["tenure"].median() if "tenure" in df else None,
        "MonthlyCharges": df["MonthlyCharges"].median() if "MonthlyCharges" in df else None,
        "TotalCharges": df["TotalCharges"].median() if "TotalCharges" in df else None,
    }
    for col, val in numeric_fill_map.items():
        if col in df:
            df[col] = df[col].fillna(val)

    # Fill missing categorical values with "Unknown"
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].fillna("Unknown")

    # 2️⃣ FEATURE ENGINEERING

    # 1. tenure_group
    if "tenure" in df:
        df["tenure_group"] = pd.cut(
            df["tenure"],
            bins=[-1, 12, 36, 60, float("inf")],
            labels=["New", "Regular", "Loyal", "Champion"]
        )

    # 2. monthly_charge_segment
    if "MonthlyCharges" in df:
        df["monthly_charge_segment"] = pd.cut(
            df["MonthlyCharges"],
            bins=[-1, 30, 70, float("inf")],
            labels=["Low", "Medium", "High"]
        )

    # 3. has_internet_service
    if "InternetService" in df:
        df["has_internet_service"] = df["InternetService"].map({
            "DSL": 1,
            "Fiber optic": 1,
            "No": 0
        }).fillna(0)

    # 4. is_multi_line_user
    if "MultipleLines" in df:
        df["is_multi_line_user"] = (df["MultipleLines"] == "Yes").astype(int)

    # 5. contract_type_code
    if "Contract" in df:
        df["contract_type_code"] = df["Contract"].map({
            "Month-to-month": 0,
            "One year": 1,
            "Two year": 2
        }).fillna(-1)

    # 3️⃣ DROP UNNECESSARY FIELDS
    # All columns that are NOT in Supabase schema must be dropped
    columns_to_drop = [
        "customerID", "gender",
        "Partner", "Dependents", "PhoneService", "MultipleLines",
        "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies",
        "PaperlessBilling", "SeniorCitizen"
    ]

    df.drop(columns=columns_to_drop, inplace=True, errors="ignore")

    # 4️⃣ SAVE TRANSFORMED DATA

    staged_path = os.path.join(staged_dir, "churn_transformed.csv")
    df.to_csv(staged_path, index=False)
    print(f"✅ Data transformed and saved at: {staged_path}")

    return staged_path


if __name__ == "__main__":
    from extract import extract_data
    raw_path = extract_data()
    transform_data(raw_path)
