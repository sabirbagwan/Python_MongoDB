import csv
from pymongo import MongoClient

#CSV to JSON Conversion

csvfile = open(r'D:\FileName.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 

db=mongo_client.DataImport
# db.sample.drop()

header= [ "Date", "Expiry", "Strike", "CE/PE", "Time", "Open", "High", "Low", "Close"]
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.Nifty.insert_one(row)