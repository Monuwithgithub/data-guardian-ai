from .missing_values import check_missing_values
from .duplicates import check_duplicates
from .outliers import detect_outliers

def generate_data_quality_report(df):
    report = {}

    report["missing_values"] = check_missing_values(df)
    report["duplicates"] = check_duplicates(df)
    report["outliers"] = detect_outliers(df)

    return report