from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(data: dict):
    try:
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]

        return {"prediction": int(prediction)}

    except Exception as e:
        return {"error": str(e)}