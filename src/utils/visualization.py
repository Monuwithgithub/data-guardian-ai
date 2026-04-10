import plotly.express as px
import streamlit as st


def show_missing_heatmap(df):
    st.markdown("### 🔍 Missing Values Heatmap")

    fig = px.imshow(
        df.isnull(),
        aspect="auto",
        title="Missing Values Heatmap"
    )

    st.plotly_chart(fig, use_container_width=True)

    missing_percent = (df.isnull().sum() / len(df)) * 100

    st.markdown("### 📊 Missing Value Percentage")
    st.dataframe(missing_percent.sort_values(ascending=False))

    


def show_distribution(df):
    st.markdown("### 📊 Data Distribution")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if numeric_cols:
        col = st.selectbox("Select column", numeric_cols)

        fig = px.histogram(df, x=col, nbins=30)

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No numeric columns found")


def show_boxplot(df):
    st.markdown("### ⚠️ Outlier Detection")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if numeric_cols:
        col = st.selectbox("Select column for boxplot", numeric_cols, key="box")

        fig = px.box(df, y=col)

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No numeric columns found")


def show_dashboard(df):
    st.subheader("📈 Data Visualization Dashboard")

    show_missing_heatmap(df)
    show_distribution(df)
    show_boxplot(df)