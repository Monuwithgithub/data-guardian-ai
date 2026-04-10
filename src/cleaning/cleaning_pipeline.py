import pandas as pd

def clean_data(df):
    report = {}

    original_shape = df.shape

    # 1. Remove duplicates
    df = df.drop_duplicates()
    report["duplicates_removed"] = original_shape[0] - df.shape[0]

    # 2. Handle missing values
    missing_before = df.isnull().sum().sum()

    # Fill numeric with mean
    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

    # Fill categorical with mode
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    missing_after = df.isnull().sum().sum()
    report["missing_values_fixed"] = missing_before - missing_after

    # 3. Simple outlier handling (IQR method)
    outliers_removed = 0

    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        before = df.shape[0]
        df = df[(df[col] >= lower) & (df[col] <= upper)]
        after = df.shape[0]

        outliers_removed += (before - after)

    report["outliers_removed"] = outliers_removed

    report["final_shape"] = df.shape

    return df, report