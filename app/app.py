import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.agent.chat_with_data import chat_with_data
import streamlit as st
import pandas as pd
from src.monitoring.report import generate_data_quality_report
from src.cleaning.cleaning_pipeline import clean_data
from src.agent.llm_explainer import generate_ai_insight
from src.utils.visualization import show_dashboard
from src.utils.pdf_generator import generate_pdf

st.markdown("""
<style>

/* Make buttons look like real buttons */
div.stButton > button {
    background-color: #45a049;
    color: white;
    font-size: 16px;
    padding: 10px 20px;
    border-radius: 8px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

/* Hover effect */
div.stButton > button:hover {
    background-color: #FFFFFF;
    transform: scale(1.05);
}

/* Download button */
div.stDownloadButton > button {
    background-color: #000000;
    color: white;
    font-size: 16px;
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: bold;
}

/* Input box styling */
input {
    border-radius: 8px !important;
}

</style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="Data Guardian AI", layout="wide")

if "cleaned_df" not in st.session_state:
    st.session_state.cleaned_df = None

if "cleaning_report" not in st.session_state:
    st.session_state.cleaning_report = None

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
    show_dashboard(df)
     
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
            st.write("Cleaning started...")
            cleaned_df, cleaning_report = clean_data(df)

            st.session_state.cleaned_df = cleaned_df
            st.session_state.cleaning_report = cleaning_report

        # ✅ SHOW CLEANED DATA (OUTSIDE BUTTON)
        if st.session_state.cleaned_df is not None:
            cleaned_df = st.session_state.cleaned_df

            st.subheader("✅ Cleaned Dataset")
            st.dataframe(cleaned_df.head())

            st.write("Original Shape:", df.shape)
            st.write("Cleaned Shape:", cleaned_df.shape)
            st.write("Total Missing Before:", df.isnull().sum().sum())
            st.write("Total Missing After:", cleaned_df.isnull().sum().sum())
            st.write("Total Rows Before:", df.shape[0])
            st.write("Total Rows After:", cleaned_df.shape[0])
            st.write("Changed Rows Preview:")
            st.dataframe(cleaned_df.tail())

            st.subheader("🧠 Cleaning Report")
            st.json(st.session_state.cleaning_report)

            st.subheader("📈 Data Quality Score")
            score = st.session_state.report.get("data_quality_score", 0)
            st.metric(label="Quality Score", value=f"{score}%")
            if score > 80:
                st.success(f"✅ Excellent Data Quality: {score}%")
            elif score > 50:
                st.warning(f"⚠️ Moderate Data Quality: {score}%")
            else:
                st.error(f"❌ Poor Data Quality: {score}%")

        # ✅ AI Insight Button
        st.subheader("🤖 AI Insight")

        if st.button("Generate AI Insight"):
          with st.spinner("Analyzing data... please wait ⏳"):
            insight = generate_ai_insight(report)
            st.session_state.insight = insight

            st.subheader("AI Insight")
            st.write(insight)

          if insight.startswith("❌"):
            st.error(insight)
          else:
             st.success("Insight Generated Successfully ✅")

        # Display in a nice box
             st.markdown(
               f"""
                <div style="
                background-color:#f9f9f9;
                padding:20px;
                border-radius:10px;
                border-left:6px solid #4CAF50;
                font-size:16px;
                line-height:1.6;
                 ">
                {insight}
                   </div>
                    """,
                unsafe_allow_html=True
        )
        if "report" in st.session_state and "insight" in st.session_state:
         if st.button("📄 Generate Report"):
           file_path = generate_pdf(st.session_state.report, st.session_state.insight)

           with open(file_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Report",
                data=f,
                file_name="data_report.pdf",
                mime="application/pdf"
            )
             
        st.subheader("💬 Chat with Your Data")

        user_question = st.text_input("Ask a question about your dataset")

        if st.button(" 🤖 Ask AI"):
           answer = chat_with_data(user_question, report)
           st.write(answer)
