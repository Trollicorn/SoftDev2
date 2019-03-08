#Team ezrael - Ivan Zhang, William Lu, and Mohammed Uddin
#SoftDev2 pd7
#K #08: Ay Mon, Go Git It From Yer Flask
#2019-03-07
'''
    Pokedex Database
    Contains Information (Name, Id, Type, Height, Weight, Weaknesses, Evolutions, etc.) of Pokemon
    Raw Data: https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
    Import Directions:
        Remove '{"pokemon":' at the beginning of the JSON file and the corresponding '}' at the end
        When Importing the JSON attach '--jsonArray' flag:
            mongoimport --db DATABASE_NAME --collection COLLECTION_NAME --drop --jsonArray --file DIRECTORY_NAME/pokedex.json
'''
import pymongo

def pokemon_type(collection, type):
    results = collection.find({"type":type})
    return(results)

def pokemon_name(collection, name):
    results = collection.find({"name":name})
    return(results)

def pokemon_weight(collection, weight):
    results = collection.find({'weight':str(weight) + " kg"})
    return(results)

def pokemon_height(collection, height):
    results = collection.find({'height':str(height) + " m"})
    return(results)

def pokemon_evolvedFrom(collection, prevEvol):
    results = collection.find({"prev_evolution.name": prevEvol})
    return(results)

def pokemon_evolvedInto(collection, nextEvol):
    results = collection.find({"next_evolution.name": nextEvol})
    return(results)
