<<<<<<< HEAD

=======
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
import pandas as pd

def check_missing_values(df: pd.DataFrame):
    missing = df.isnull().sum()
    percent = (missing / len(df)) * 100

    result = pd.DataFrame({
        "column": df.columns,
        "missing_count": missing.values,
        "missing_percent": percent.values
    })

<<<<<<< HEAD
    return result.sort_values(by="missing_percent", ascending=False)
=======
    return result.sort_values(by="missing_percent", ascending=False)
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
