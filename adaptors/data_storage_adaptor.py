import ports.mongo_port

def read_one_temperature(timestamp: str):
    db = ports.mongo_port.get_db()
    collection = db.get_collection("temperatures")
    return collection.find_one({"timestamp": timestamp})

def delete_one_temperature(timestamp: str):
    db = ports.mongo_port.get_db()
    collection = db.get_collection("temperatures")
    return collection.delete_one({"timestamp": timestamp})

def create_temperature(data):
    db = ports.mongo_port.get_db() 
    collection = db.get_collection("temperatures")
    return collection.insert_one(data).inserted_id
