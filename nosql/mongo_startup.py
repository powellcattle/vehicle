import pymongo

def global_init() -> object:
    conn_str = "mongodb://spowell:n2329w@localhost:27017/?authSource=vehicle_db"
    cl = pymongo.MongoClient(conn_str)
    return cl['vehicle_db']
