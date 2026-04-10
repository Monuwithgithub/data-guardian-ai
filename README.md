<<<<<<< HEAD
# data-guardian-ai
=======
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

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/data-guardian-ai.git

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




>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
