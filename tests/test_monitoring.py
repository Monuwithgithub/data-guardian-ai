<<<<<<< HEAD
from turtle import st

=======
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
import pandas as pd
from src.monitoring.report import generate_data_quality_report

df = pd.read_csv("data/titanic.csv")

report = generate_data_quality_report(df)

print("\n===== MISSING VALUES =====\n", report["missing_values"])
print("\n===== DUPLICATES =====\n", report["duplicates"])
print("\n===== OUTLIERS =====\n", report["outliers"])

from src.cleaning.cleaning_pipeline import clean_data

cleaned_df, cleaning_report = clean_data(df)

<<<<<<< HEAD
print("\n===== CLEANING REPORT =====\n", cleaning_report)
st.write("Original Shape:", df.shape)
st.write("Cleaned Shape:", cleaned_df.shape)
=======
print("\n===== CLEANING REPORT =====\n", cleaning_report)
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
