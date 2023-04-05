from pymongo import MongoClient
from appsettings import database

async def getconection(collection):
    client = MongoClient(database['url'])
    db = client[database['database']]
    return db[collection]