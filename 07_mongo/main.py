# azrael -- Jason Tung and Mohammed Uddin
#
# SoftDev2 pd7
#
# K #07: Import/Export Bank
#
# 2019-03-01

# --------DB INFO--------
# NAME: POKEMON GO POKEDEX
# CONTAINS INFORMATION FOR EACH POKEMON IN POKEMON GO
# NOTE: WE ONLY PARSED INFORMATION PERTAINING TO REAL POKEMON GAMES!!!
# LINK: https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
# IMPORT MECHANISM: parsed pokedex.json from db.pokedex_unparsed in json_setup.pymongo
# imported pokedex_parsed.json as db.azrael.


import pymongo

server_addr = "jayy.mooo.com"
connection = pymongo.MongoClient(server_addr)
db = connection.test
connection = db.azrael


# for k in connection.find({}):
#     print(k)


def find_pokemans(**kwargs):
    # POSSIBLE ARGS: num, name, type, height, height_updown, weight, weight_updown, weaknesses, evolutions
    find_query = {}
    args = {"num": None, "name": None, "type": None, "height": None,
            "weight": None, "weaknesses": None, "evolutions": None}
    for k in args.keys():
        args[k] = kwargs.get(k, None)
        if args[k] is not None:
            if k == "evolutions":
                find_query["$or"] = [{"next_evolution": {"$elemMatch": {"name": args[k]}}},
                                     {"prev_evolution": {"$elemMatch": {"name": args[k]}}}]
            elif k in ["weaknesses", 'type']:
                find_query[k] = {'$in': args[k]}
            else:
                find_query[k] = args[k]
    print("QUERY:", find_query)
    print("-+-+-")
    for k in connection.find(find_query):
        print("name: ", k['name'])
        for ele in args:
            if args[ele] is not None:
                if ele == "evolutions":
                    ret_str = "evolutions: "
                    prefixes = ["next", "prev"]
                    for pref in prefixes:
                        try:
                            ret_str += [x["name"] for x in k[pref + "_evolution"]] + ", "
                        except:
                            pass
                elif ele != "name":
                    print(ele + ": ", k[ele])
        print("-+-+-")


# print("EVOLUTION: CHARIZARD")
print("~~~~~~~~~~~~~~~~~~")
find_pokemans(evolutions="Charizard")
# print("HEIGHT: 1.19 m, TYPE: FLYING")
print("~~~~~~~~~~~~~~~~~~")
find_pokemans(height='1.19 m', type=['Flying'])
# print("NUM: >050, HEIGHT: >1.00 m, TYPE: WATER OR ICE, WEAKNESS: BUG OR FIRE")
print("~~~~~~~~~~~~~~~~~~")
find_pokemans(num={"$gt": "050"}, height={"$gt": "1.00 m"}, type=['Water', 'Ice'], weaknesses=['Bug', 'Fire'])
