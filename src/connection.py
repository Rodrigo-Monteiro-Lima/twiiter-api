from pymongo import MongoClient

client = MongoClient("mongodb://root:root@mongo:27017/")

db = client.test

trends_collection = db.trends
