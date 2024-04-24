from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_ENV = os.getenv('MONGO_URI')

client = MongoClient(MONGO_ENV)
db = client["fastapi"]
coll = db["pars"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)