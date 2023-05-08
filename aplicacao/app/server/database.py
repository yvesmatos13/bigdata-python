from pymongo import MongoClient
from appsettings import database

def getconection():
    client = MongoClient(database['url'])
    db = client[database['database']]
    return db[database['collection']]