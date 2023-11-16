from pymongo import MongoClient


# client = MongoClient(host='mongodb://localhost:27017/')
client = MongoClient(host='test_mongodb', port=27017)
db = client['mydatabase']
collection = db['formcollection']