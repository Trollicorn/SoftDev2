import pymongo

SERVER_ADDR = "157.230.51.119"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db. restaurants
