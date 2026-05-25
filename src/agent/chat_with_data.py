import requests

from src.utils.config import get_openai_api_key


def chat_with_data(question, report):
    API_KEY = get_openai_api_key()

    if not API_KEY:
        return (
            "❌ API key not found. Set OPENAI_API_KEY in a local .env file, "
            "or add it under Streamlit Cloud → App settings → Secrets."
        )

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