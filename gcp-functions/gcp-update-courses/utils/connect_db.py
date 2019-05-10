import os
import pymongo
import datetime
import json
from bson import objectid

class Datastore:
  def __init__(self):
    username = os.environ["MONGO_USER"]
    password = os.environ["MONGO_PASS"]
    self.url = "mongodb://{}:{}@cluster0-shard-00-00-rpoft.gcp.mongodb.net:27017,cluster0-shard-00-01-rpoft.gcp.mongodb.net:27017,cluster0-shard-00-02-rpoft.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true".format(username, password)

  def update_record(self, id, source, target):
    client = pymongo.MongoClient(self.url)
    mydb = client["universitas_library"]
    mycol = mydb["kanban"]

    mycol.update_one({"id": source}, {"$pull": {"cards": objectid.ObjectId(id)}})
    x = mycol.update_one({"id": target}, {"$push": {"cards": objectid.ObjectId(id)}})
    return x.modified_count