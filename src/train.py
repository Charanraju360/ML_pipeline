import pandas as pd
import os
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

os.makedirs("models", exist_ok=True)

# load data
df = pd.read_csv("data/processed/data.csv")

X = df[["Pclass", "Age", "SibSp", "Parch", "Fare"]]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 🔥 MLflow tracking starts here
with mlflow.start_run():

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # log parameters
    mlflow.log_param("model", "LogisticRegression")
    mlflow.log_param("max_iter", 200)

    # log metric
    mlflow.log_metric("accuracy", acc)

    # log model
    mlflow.sklearn.log_model(model, "model")

    # save locally
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

print("Model trained & logged to MLflow")