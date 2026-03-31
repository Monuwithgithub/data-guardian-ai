import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import pandas as pd
from src.monitoring.report import generate_data_quality_report
from src.cleaning.cleaning_pipeline import clean_data


if "cleaned_df" not in st.session_state:
    st.session_state.cleaned_df = None

if "cleaning_report" not in st.session_state:
    st.session_state.cleaning_report = None
# Page config
st.set_page_config(page_title="Data Guardian AI", layout="wide")


# Title
st.title("🛡️ Data Guardian AI")
st.write("Autonomous Data Quality & Debugging System")

# File upload
uploaded_file = st.file_uploader("📂 Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Preview
    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    # ✅ SCAN BUTTON
    if st.button("🔍 Scan Data"):
        report = generate_data_quality_report(df)
        st.session_state.report = report

    # ✅ SHOW REPORT (OUTSIDE BUTTON)
    if "report" in st.session_state:
        report = st.session_state.report

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🚨 Missing Values")
            st.dataframe(report["missing_values"])

        with col2:
            st.subheader("🔁 Duplicates")
            st.write(f"Total Duplicates: {report['duplicates']['total_duplicates']}")

        st.subheader("⚠️ Outliers")
        st.json(report["outliers"])

        # ✅ AUTO CLEAN BUTTON (SEPARATE)
        if st.button("🧹 Auto Clean Data"):
            cleaned_df, cleaning_report = clean_data(df)

            st.session_state.cleaned_df = cleaned_df
            st.session_state.cleaning_report = cleaning_report

    # ✅ SHOW CLEANED DATA (OUTSIDE BUTTON)
    if st.session_state.cleaned_df is not None:
        st.subheader("✅ Cleaned Dataset")
        st.dataframe(st.session_state.cleaned_df.head())

        st.subheader("🧠 Cleaning Report")
        st.json(st.session_state.cleaning_report)