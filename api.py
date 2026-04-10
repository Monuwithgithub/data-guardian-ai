from fastapi import FastAPI
import pandas as pd
from src.monitoring.report import generate_data_quality_report
from src.cleaning.cleaning_pipeline import clean_data

app = FastAPI()


@app.post("/scan")
def scan_data(data: dict):
    df = pd.DataFrame(data)
    report = generate_data_quality_report(df)
    return report


@app.post("/clean")
def clean(data: dict):
    df = pd.DataFrame(data)
    cleaned_df, report = clean_data(df)
    return {
        "cleaned_data": cleaned_df.to_dict(),
        "report": report
    }


@app.post("/insight")
def insight(data: dict):
    from src.agent.llm_explainer import generate_ai_insight

    return {"insight": generate_ai_insight(data)}