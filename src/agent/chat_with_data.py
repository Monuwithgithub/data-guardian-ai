import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def chat_with_data(question, report):
    API_KEY = os.getenv("OPENAI_API_KEY")

    prompt = f"""
    You are a data analyst.

    Dataset summary:
    {report}

    Answer this question:
    {question}
    """

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    if response.status_code != 200:
        return f"Error from OpenAI API: {response.text}"

    return response.json()["choices"][0]["message"]["content"]