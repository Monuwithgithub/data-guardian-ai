from .missing_handler import handle_missing_values
from .outlier_handler import handle_outliers

def clean_data(df):
    final_report = {}

    # Step 1: Handle missing values
    df, missing_report = handle_missing_values(df)
    final_report["missing"] = missing_report

    # Step 2: Handle outliers
    df, outlier_report = handle_outliers(df)
    final_report["outliers"] = outlier_report

    return df, final_report