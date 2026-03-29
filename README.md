# 📊 Data Lineage & Impact Analysis System

## 🚀 Overview
This project simulates a real-world data pipeline and implements a **data lineage tracking system** to trace how data flows across multiple transformation stages.

It enables **impact analysis**, helping answer:
> "If a dataset changes, what downstream systems are affected?"

---

## 🧱 Architecture

Raw Data → Cleaned Data → Aggregated Data

Example Flow:
orders_raw → orders_cleaned → revenue_summary

---

## ⚙️ Tech Stack

- Python
- Pandas
- SQLite
- NetworkX
- Streamlit

---

## 📂 Project Structure

data-lineage-project/
│
├── data/
│ ├── raw/
│ ├── processed/
│
├── scripts/
│ ├── clean_orders.py
│ ├── transform_customers.py
│ ├── aggregate_revenue.py
│ ├── lineage_tracker.py
│
├── db/
│ ├── lineage.db
│
├── app/
│ ├── streamlit_app.py
│
├── main.py
└── README.md


---

## 🔄 Data Pipeline

1. **Data Cleaning**
   - Removes duplicates
   - Handles missing values

2. **Transformation**
   - Standardizes customer data

3. **Aggregation**
   - Computes revenue per customer

---

## 🔗 Data Lineage Tracking

The system logs:
- Source dataset
- Target dataset
- Transformation applied
- Timestamp

Stored in SQLite database (`lineage.db`)

---

## 📊 Key Features

### ✅ Lineage Tracking
Tracks dataset dependencies across pipeline stages

### ✅ Impact Analysis
- Identify downstream dependencies
- Identify upstream sources

### ✅ Interactive UI
- Select dataset
- View lineage relationships

---

## 🖥️ Sample Output

### Downstream Impact
orders_cleaned → revenue_summary

### Upstream Sources
orders_cleaned ← orders_raw

---

## ▶️ How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run pipeline
python scripts/clean_orders.py
python scripts/transform_customers.py
python scripts/aggregate_revenue.py

### 3. Launch UI
streamlit run app/streamlit_app.py


---

## 📈 Future Improvements

- Column-level lineage tracking
- Real-time pipeline monitoring
- Integration with Airflow
- Advanced data quality metrics

---

## 💼 Resume Highlight

Built a metadata-driven data lineage system enabling impact analysis and dependency tracking using graph-based modeling.

---

## 👤 Author
Kemi Awolola