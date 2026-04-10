def validate_schema(df, expected_schema: dict):
    issues = []

    for col, expected_type in expected_schema.items():
        if col not in df.columns:
            issues.append(f"Missing column: {col}")
        else:
            if df[col].dtype != expected_type:
                issues.append(
                    f"Column {col}: Expected {expected_type}, Got {df[col].dtype}"
                )

<<<<<<< HEAD
    return issues
=======
    return issues
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
