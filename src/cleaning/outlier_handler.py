import numpy as np

def handle_outliers(df):
    df_cleaned = df.copy()
    report = {}

    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        before = df[col].copy()

        # Cap outliers
        df_cleaned[col] = np.where(df[col] < lower, lower,
                           np.where(df[col] > upper, upper, df[col]))

        report[col] = {
            "lower_bound": lower,
            "upper_bound": upper,
            "action": "capped"
        }

    return df_cleaned, report