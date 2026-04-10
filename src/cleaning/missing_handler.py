import pandas as pd

def handle_missing_values(df):
    df_cleaned = df.copy()
    report = {}

    for col in df.columns:
        missing_percent = df[col].isnull().mean() * 100

        if missing_percent == 0:
            continue

        # Decision logic
        if df[col].dtype == 'object':
            df_cleaned[col].fillna(df[col].mode()[0], inplace=True)
            method = "mode"

        else:
            if missing_percent < 30:
                df_cleaned[col].fillna(df[col].median(), inplace=True)
                method = "median"
            else:
                df_cleaned[col].fillna(df[col].mean(), inplace=True)
                method = "mean"

        report[col] = {
            "missing_percent": missing_percent,
            "method_used": method
        }

    return df_cleaned, report