import pandas as pd
from pymongo import MongoClient
import glob


filepath = r"D:\MongoDB"

client = MongoClient("mongodb://localhost:27017")
for file in glob.glob(filepath + "\*.csv"):
    df = pd.read_csv(file)
    data = df.to_dict(orient="records")
    db = client["volume"]
    db.Nifty.insert_many(data)
    print(file)

print('importing completed!')


