# 🏗️ Real Estate Data Engineering Pipeline

This project demonstrates how data engineering strategies — including ETL pipelines, Airbyte integrations, and Python data processing — can transform fragmented property data into a unified, reliable source of truth for business insights.

---

## 🚀 Project Overview

Metropeak data is often stored across multiple platforms and databases.  
This project builds a **modern data pipeline** that:

- Extracts data from multiple platforms (databases, APIs, files)
- Transforms and cleans it using **Python + pandas**
- Loads it into a centralized **Postgresql database** 
<!-- - Loads it into a centralized **data warehouse** for analytics -->
- Enables **real-time access** via dashboards or APIs

---

## ⚙️ Tech Stack

| Layer          | Tool                         | Purpose                               |
| -------------- | ---------------------------- | ------------------------------------- |
| Extraction     | **Python**                   | Ingest data from multiple sources     |
| Transformation | **Python (pandas)**          | Clean, validate, and standardize data |
| Storage        | **PostgreSQL / Snowflake**   | Centralized warehouse                 |
| Orchestration  | **Airflow / dbt (optional)** | Schedule and manage pipeline runs     |
| Visualization  | **Power BI / Looker Studio** | Real-time dashboards and reports      |

---

## 🧩 ETL Pipeline Workflow

1. **Extract:**  
   Use Airbyte to connect to CRMs, listing APIs, and local CSVs.

2. **Transform:**  
   Clean and merge datasets using pandas:
   ```python
   df = pd.read_csv("properties.csv")
   df = df.dropna().drop_duplicates()
   df["price_per_sqft"] = df["price"] / df["sqft"]
   ```
