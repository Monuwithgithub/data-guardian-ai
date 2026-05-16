from dotenv import load_dotenv
import requests
import os
load_dotenv(override=True) 

def generate_ai_insight(report):
    """
    Generate AI insights using OpenAI-compatible API
    """

    try:
        API_KEY = os.getenv("OPENAI_API_KEY")
          
        if not API_KEY:
            return "❌ API key not found. Please set OPENAI_API_KEY."
            

        API_URL = "https://api.openai.com/v1/chat/completions"

        prompt = f"""
        You are a professional data analyst.

        Analyze the dataset quality:

        - Data Quality Score: {report.get('data_quality_score')}%
        - Missing Values: {report.get('missing_values')}
        - Duplicates: {report.get('duplicates')}
        - Outliers: {report.get('outliers')}
           """

        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are a helpful data analyst."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7
            }
        )
        print("DEBUG KEY:", API_KEY)

        if response.status_code != 200:
            return f"❌ API Error: {response.text}"

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Error: {str(e)}"