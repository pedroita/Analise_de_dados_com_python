
import pymongo
connection_string = "mongodb+srv://campos2512:campos2512@cluster0.vfp6e.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoCliente(connection_string)

db = client["mydatabase"]

collection = db["mycollection"]