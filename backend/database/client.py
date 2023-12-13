from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from environment import variables

client = MongoClient(
    "mongodb+srv://davld7:JH3YhKgI0a32x3Ea@cluster0.dvycjzp.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

database = client.get_database("netflix")
contacts_collection = database.get_collection("contacts")
