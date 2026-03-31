import pandas as pd

def check_missing_values(df: pd.DataFrame):
    missing = df.isnull().sum()
    percent = (missing / len(df)) * 100

    result = pd.DataFrame({
        "column": df.columns,
        "missing_count": missing.values,
        "missing_percent": percent.values
    })

    return result.sort_values(by="missing_percent", ascending=False)