import pandas as pd
import os

# create output folder if not exists
os.makedirs("data/processed", exist_ok=True)

# load data
df = pd.read_csv("data/raw/data.csv")

# simple preprocessing
df = df.dropna()

# save processed data
df.to_csv("data/processed/data.csv", index=False)

print("Preprocessing done. File saved to data/processed/data.csv")