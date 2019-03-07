# azrael -- Jason Tung and Mohammed Uddin
#
# SoftDev2 pd7
#
# K #07: Import/Export Bank
#
# 2019-03-01
import json

import pymongo

server_addr = "0.0.0.0"
connection = pymongo.MongoClient(server_addr)
db = connection.test
connection = db.pokedex_unparsed

id = 1
pkmon_list = connection.find_one({})["pokemon"]
with open("pokedex_parsed.json", "w") as f:
    f.write("[")
    for pkmon in pkmon_list:
        f.write(json.dumps(pkmon))
        if id < 151:
            f.write(",\n")
        id+=1
    f.write("]")

collection = db.azrael
collection.drop()
f=open("pokedex_parsed.json","r")
json_data = f.read()
f.close()
data = json.loads(json_data)

collection.insert_many(data)
