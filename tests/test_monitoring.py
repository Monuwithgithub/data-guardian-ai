import pandas as pd
from src.monitoring.report import generate_data_quality_report

df = pd.read_csv("data/titanic.csv")

report = generate_data_quality_report(df)

print("\n===== MISSING VALUES =====\n", report["missing_values"])
print("\n===== DUPLICATES =====\n", report["duplicates"])
print("\n===== OUTLIERS =====\n", report["outliers"])

from src.cleaning.cleaning_pipeline import clean_data

cleaned_df, cleaning_report = clean_data(df)

print("\n===== CLEANING REPORT =====\n", cleaning_report)