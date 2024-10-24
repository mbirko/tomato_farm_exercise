import sys
import ports.mongo_port 
from pprint import pprint


def main(args):
    db = ports.mongo_port.get_db(database_name="dota")
    collection_names = db.list_collection_names()
    print("Collections in database:")
    pprint(collection_names)
    for collection in collection_names:
        print(f"Collection: {collection}")
        number_of_documents = db[collection].count_documents({})
        print(f"Number of documents: {number_of_documents}")
        print(f"indexes:")
        pprint(list(db[collection].list_indexes()))


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
