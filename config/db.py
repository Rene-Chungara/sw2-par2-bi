from pymongo import MongoClient

def get_database():
    uri = "mongodb://mongo:PyupIDyhqGSIBwHdxiMUEzjCoisLXtKE@trolley.proxy.rlwy.net:27877"
    client = MongoClient(uri)
    return client["bi_textileria"]
