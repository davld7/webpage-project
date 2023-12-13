from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from environment import variables

client = MongoClient(variables.uri, server_api=ServerApi('1'))

database = client.get_database("netflix")
contacts_collection = database.get_collection("contacts")
