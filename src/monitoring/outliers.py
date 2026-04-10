import numpy as np

def detect_outliers(df):
    outlier_summary = {}

    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower) | (df[col] > upper)]

        outlier_summary[col] = {
            "outlier_count": len(outliers),
            "lower_bound": lower,
            "upper_bound": upper
        }

<<<<<<< HEAD
    return outlier_summary
=======
    return outlier_summary
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
