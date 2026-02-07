# Weather Data Pipeline 🌦️

An end-to-end **ETL data pipeline** that extracts weather data from an external API, transforms it into a structured format, and loads it into **PostgreSQL**, orchestrated using **Apache Airflow** and containerized with **Docker**.

This project showcases core data engineering skills such as API ingestion, transformation logic, orchestration, and production-style project structure.

---

## 🚀 Project Overview

The pipeline performs the following steps:

1. **Extract** weather data from a public weather API
2. **Transform** raw API responses into clean, analytics-ready data
3. **Load** processed data into PostgreSQL tables
4. Orchestrate the workflow using **Apache Airflow DAGs**

---

## 🧱 Architecture

Weather API
↓
Extract (Python)
↓
Transform (Python)
↓
Load (PostgreSQL)
↓
Airflow DAG (Scheduling & Monitoring)

yaml
Copy code

---

## 🛠 Tech Stack

- **Python**
- **Apache Airflow**
- **PostgreSQL**
- **SQL**
- **Docker & Docker Compose**
- **Git & GitHub**

---

## 📁 Project Structure

WEATHER_PIPELINE/
│
├── dags/
│ ├── weather_pipeline_dags.py # Airflow DAG definition
│ └── src/ # DAG task logic
│
├── src/
│ ├── config.py # API & DB configuration
│ ├── extract.py # Extract weather data
│ ├── transform.py # Data cleaning & transformation
│ ├── load.py # Load data into PostgreSQL
│ └── init.py
│
├── sql/ # SQL scripts (optional)
├── logs/ # Airflow logs
├── scripts/ # Helper scripts
│
├── docker-compose.yml
├── requirements.txt
├── .env # Environment variables (ignored)
└── README.md

yaml
Copy code

---

## 📥 Extract

- Fetches current weather data from an external API
- Handles JSON responses and missing fields
- Supports configurable locations via `config.py`

---

## 🔄 Transform

- Normalizes temperature, humidity, and weather metrics
- Converts timestamps to standard formats
- Prepares data for relational storage

---

## 📤 Load

- Inserts transformed data into PostgreSQL tables
- Ensures schema consistency and data integrity

---

## ⏱ Orchestration with Airflow

- DAG defined in `weather_pipeline_dags.py`
- Tasks:
  - Extract
  - Transform
  - Load
- Supports scheduled execution and retries

---

## ▶️ How to Run

### 1. Clone repository
```bash
git clone https://github.com/Robin6551/weather_pipeline.git
cd weather_pipeline
2. Configure environment variables
Create a .env file:

env
Copy code
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=weather
WEATHER_API_KEY=your_api_key
3. Start services
bash
Copy code
docker-compose up -d
4. Access Airflow UI
arduino
Copy code
http://localhost:8080
Trigger the Weather Pipeline DAG.

🎯 Key Learnings
API-based data ingestion

Airflow DAG orchestration

ETL pipeline design

Dockerized data pipelines

PostgreSQL integration

🔮 Future Improvements
Historical weather ingestion

Incremental loading

Data quality checks

Cloud deployment

Analytics dashboards

👤 Author
Robin
Aspiring Data Engineer
GitHub: https://github.com/Robin6551

yaml
Copy code

---

## 4️⃣ Commit README
```powershell
git add README.md .gitignore
git commit -m "Add Weather pipeline README"
git push
