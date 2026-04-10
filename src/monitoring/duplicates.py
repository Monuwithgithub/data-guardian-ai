def check_duplicates(df):
    total_duplicates = df.duplicated().sum()
    duplicate_rows = df[df.duplicated()]

    return {
        "total_duplicates": total_duplicates,
        "duplicate_sample": duplicate_rows.head()
<<<<<<< HEAD
    }
=======
    }
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
