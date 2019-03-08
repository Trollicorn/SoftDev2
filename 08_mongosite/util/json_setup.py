import json

import pymongo

def setup(db):
    id = 1
    connection = db.pokemons

    pkmon_list = connection.find_one({})["pokemon"]
    with open("pokedex_parsed.json", "w") as f:
        f.write("[")
        for pkmon in pkmon_list:
            f.write(json.dumps(pkmon))
            if id < 151:
                f.write(",\n")
            id+=1
        f.write("]")

    collection =db.ezrael
    collection.drop()
    f=open("pokedex_parsed.json","r")
    json_data = f.read()
    f.close()
    data = json.loads(json_data)

    collection.insert_many(data)
