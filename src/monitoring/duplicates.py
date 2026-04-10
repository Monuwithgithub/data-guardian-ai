def check_duplicates(df):
    total_duplicates = df.duplicated().sum()
    duplicate_rows = df[df.duplicated()]

    return {
        "total_duplicates": total_duplicates,
        "duplicate_sample": duplicate_rows.head()
    }
