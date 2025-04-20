import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os 

db_password = os.environ.get("MONGODB_PASSWORD")


client = pymongo.MongoClient(f"mongodb+srv://mayanku:{db_password}@cluster0.uqi8x0h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.sample_mflix
collection = db.movies

items = collection.find().limit(5)

for item in items:
    print(item)

