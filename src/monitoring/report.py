from .missing_values import check_missing_values
from .duplicates import check_duplicates
from .outliers import detect_outliers

def generate_data_quality_report(df):
    print("Function started 🚀")
    report = {}

    # Missing
    missing = df.isnull().sum()
    total_missing = missing.sum()
    report["missing_values"] = missing.reset_index()
    
    # Duplicates
    duplicates = df.duplicated().sum()
    report["duplicates"] = {"total_duplicates": duplicates}

    # Outliers
    outliers = {}
    num_cols = df.select_dtypes(include=['number']).columns
    total_outliers = 0

    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        count = ((df[col] < lower) | (df[col] > upper)).sum()
        outliers[col] = int(count)
        total_outliers += count
        print("==== DEBUG START ====")
        print("Rows:", df.shape[0])
        print("Cols:", df.shape[1])
        print("Total Missing:", total_missing)
        print("Duplicates:", duplicates)
        print("Total Outliers:", total_outliers)
        print("Num Numeric Cols:", len(num_cols))
        print("==== DEBUG END ====")
    # ✅ OUTSIDE LOOP
    report["outliers"] = outliers

    print("Reached scoring ✅")  # ADD THIS

    # Scoring
    total_cells = df.shape[0] * df.shape[1]

    missing_pct = total_missing / total_cells if total_cells > 0 else 0
    duplicate_pct = duplicates / df.shape[0] if df.shape[0] > 0 else 0

    if len(num_cols) > 0:
        outlier_pct = total_outliers / (df.shape[0] * len(num_cols))
    else:
        outlier_pct = 0

    issue_score = (missing_pct * 0.4) + (duplicate_pct * 0.3) + (outlier_pct * 0.3)

    quality_score = int((1 - issue_score) * 100)
    quality_score = max(0, min(100, quality_score))

    report["data_quality_score"] = quality_score

    return report   # ✅ ONLY HERE