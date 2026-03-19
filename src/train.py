import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# create models folder
os.makedirs("models", exist_ok=True)

# load processed data
df = pd.read_csv("data/processed/data.csv")

# simple feature selection (Titanic example)
X = df[["Pclass", "Age", "SibSp", "Parch", "Fare"]]
y = df["Survived"]

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# save model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved to models/model.pkl")