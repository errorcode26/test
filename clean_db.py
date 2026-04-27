from config import MONGO_URI
from pymongo import MongoClient
import certifi
db = MongoClient(MONGO_URI, tlsCAFile=certifi.where()).get_database('indialims')
db.records.delete_many({})
db.users.delete_many({"user_id": {"$ne": "bootstrap-admin-01"}})
print('Cleaned')