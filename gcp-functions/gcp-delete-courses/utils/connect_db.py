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

  def delete_single_record(self, id):
    client = pymongo.MongoClient(self.url)
    mydb = client["universitas_library"]
    # kanban = mydb["kanban"]
    projects = mydb["projects"]

    try:
      x = projects.delete_one({"_id": objectid.ObjectId(id)})
      return x
    except:
      return "An error occured"
