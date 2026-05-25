"""Load secrets from env, .env (local), or Streamlit Cloud secrets."""

import os
from pathlib import Path

from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_ENV_LOADED = False


def _load_dotenv_once() -> None:
    global _ENV_LOADED
    if _ENV_LOADED:
        return
    load_dotenv(_PROJECT_ROOT / ".env", override=False)
    _ENV_LOADED = True


def _from_streamlit_secrets() -> str | None:
    try:
        import streamlit as st

        if "OPENAI_API_KEY" in st.secrets:
            return st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass
    return None


def get_openai_api_key() -> str | None:
    """
    Resolve OpenAI API key for local dev and Streamlit Cloud.

    Priority: environment variable → Streamlit secrets → .env file
    """
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key.strip()

    key = _from_streamlit_secrets()
    if key:
        return key.strip()

    _load_dotenv_once()
    key = os.getenv("OPENAI_API_KEY")
    return key.strip() if key else None
