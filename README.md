
🛡️ Data Guardian AI

Autonomous Data Quality & Debugging System

An AI-powered system to automatically analyze, detect, and clean data quality issues such as missing values, duplicates, and outliers. Built with a modular pipeline and an interactive Streamlit UI.

🚀 Features: 

📊 Data Quality Analysis

Missing values detection

Duplicate records identification

Outlier detection

🧹 Automated Data Cleaning

Handles missing values

Removes duplicates

Treats outliers

🤖 AI-Powered Insights (Planned / In Progress)

LLM-based data quality explanations

RAG-based intelligent reporting

AI Agent for autonomous decision-making

🖥️ Interactive UI

Upload dataset (CSV)

View reports instantly

Clean data with one click

🏗️ Project Structure

Data-Guardian-AI/

│

├── app/

│   └── app.py                # Streamlit UI

│

├── src/

│   ├── monitoring/

│   │   └── report.py        # Data quality report generation

│   │

│   ├── cleaning/

│   │   ├── cleaning_pipeline.py

│   │   ├── missing_handler.py

│   │   ├── outlier_handler.py

│   │   └── duplicate_handler.py

│

├── data/

│   └── titanic.csv          # Sample dataset

│

├── requirements.txt

└── README.md

UI Immages :

<img width="1885" height="871" alt="image" src="https://github.com/user-attachments/assets/048ef926-93cd-459e-a25b-80e944264e28" />

<img width="1868" height="853" alt="image" src="https://github.com/user-attachments/assets/17f6e6ac-0a90-45e1-9383-006d9883fab4" />

<img width="1881" height="822" alt="image" src="https://github.com/user-attachments/assets/a9d514d0-9d16-49d6-8dd5-ddfe66eaf9f7" />

<img width="1547" height="867" alt="image" src="https://github.com/user-attachments/assets/602c4ecf-0889-4d86-9f05-77009740b2cd" />

Project Demo :

https://drive.google.com/file/d/1kQzjyuHRPABLJnxvQqm_wpODk2eGT6on/view?usp=drive_link

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone [https:https://github.com/Monuwithgithub/data-guardian-ai

cd data-guardian-ai

2️⃣ Create virtual environment (recommended)

python -m venv venv

venv\Scripts\activate   # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

▶️ Run the Application

streamlit run app/app.py

Then open in browser:

http://localhost:8501

🔐 API key (local + Streamlit Cloud)

The OpenAI key must **not** be committed to GitHub. Use one of these:

**Local development** — create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-your-key-here
```

**Streamlit Cloud** — after you deploy, open your app on [share.streamlit.io](https://share.streamlit.io), go to **App settings → Secrets**, and paste:

```toml
OPENAI_API_KEY = "sk-your-key-here"
```

Save and reboot the app. The deployed app reads the key from Streamlit secrets (not from `.env`, which is not uploaded).

See `.streamlit/secrets.toml.example` for the same format used locally (copy to `.streamlit/secrets.toml` if you prefer secrets over `.env`).

🧠 How It Works

Upload a dataset (CSV)

Click Scan Data → Generates quality report

Click Auto Clean Data → Cleans dataset automatically

View cleaned data + report

🛠️ Tech Stack

Languages: Python

Libraries: Pandas, NumPy

Visualization/UI: Streamlit

AI (Planned): LLMs, RAG, AI Agents

📌 Future Improvements

✅ Intelligent missing value imputation (ML-based)

✅ LLM-generated data insights

✅ Data quality scoring system

✅ Export cleaned dataset

✅ Dashboard analytics


Live Demo : https://data-guardian-ai-wpe2wu9aaaw7n3wy6jeywu.streamlit.app/
