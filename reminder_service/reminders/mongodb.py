from pymongo import MongoClient
from django.conf import settings

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(settings.MONGO_DB_SETTINGS["HOST"])
        self.db = self.client[settings.MONGO_DB_SETTINGS["DATABASE_NAME"]]

    def get_collection(self, collection_name):
        return self.db[collection_name]
