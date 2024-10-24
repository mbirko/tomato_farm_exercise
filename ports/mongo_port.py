import pymongo


def get_db(database_name:str = "tomato_db"):
    client = pymongo.MongoClient("mongodb://root:example@localhost:27018/?authSource=admin") 
    db = client[database_name]
    return db

