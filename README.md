# 🚀 End-to-End MLOps Pipeline (Titanic Prediction)

## 📌 Overview
This project demonstrates a complete **MLOps pipeline** including:
- Data preprocessing
- Model training
- Experiment tracking
- Pipeline automation
- API deployment
- Frontend UI for predictions

---

## 🏗️ Architecture

User → Frontend UI → FastAPI → ML Model → MLflow  
Prefect → Pipeline Automation  
DVC → Data & Pipeline Versioning  

---

## 🛠️ Tech Stack

- Python  
- DVC  
- MLflow  
- Prefect  
- FastAPI  
- Scikit-learn  
- HTML / JavaScript  

---

## 📁 Project Structure
ML_pipeline/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── models/
│ └── model.pkl
│
├── src/
│ ├── preprocess.py
│ ├── train.py
│ ├── pipeline.py
│ └── api.py
│
├── frontend/
│ └── index.html
│
├── dvc.yaml
├── requirements.txt
└── README.md

---

## ⚙️ Setup

### 1. Clone repo
```bash
git clone https://github.com/Charanraju360/ML_pipeline.git
cd ML_pipeline
```

---

### 2. Create virtual environment
python -m venv venv
Activate:
.\venv\Scripts\activate

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
▶️ Run Project
Step 1: Start MLflow
```bash
mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns \
--host 0.0.0.0 \
--port 5000 \
--workers 1
```
Open:
```bash
http://127.0.0.1:5000
```
Step 2: Run Pipeline
```bash
python src/pipeline.py
```
Step 3: Start API
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000
```
Open:

http://127.0.0.1:8000/docs
Step 4: Run Frontend
```bash
cd frontend
python -m http.server 5500
```
Open:
```bash
http://127.0.0.1:5500
```

```bash
🧪 Sample Input
{
  "Pclass": 3,
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25
}
```
---
✅ Features
End-to-end ML pipeline

Automated workflow (Prefect)

Experiment tracking (MLflow)

Data versioning (DVC)

REST API (FastAPI)

Frontend UI
---
