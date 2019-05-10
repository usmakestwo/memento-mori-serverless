import os
import pymongo
import datetime
import json
import random
from bson import json_util

class Datastore:
  def __init__(self):
    username = os.environ["MONGO_USER"]
    password = os.environ["MONGO_PASS"]
    self.url = "mongodb://{}:{}@cluster0-shard-00-00-rpoft.gcp.mongodb.net:27017,cluster0-shard-00-01-rpoft.gcp.mongodb.net:27017,cluster0-shard-00-02-rpoft.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true".format(username, password)

  def insert_record(self, name, description, path, uploaded=True):
    client = pymongo.MongoClient(self.url)
    mydb = client["universitas_library"]
    mycol = mydb["projects"]

    single_project = {
      "id": int(random.random() * 100000),
      "createdAt": datetime.datetime.now(),
      "title": name,
      "description": description,
      "path": "https://github.com/" + path.lower(),
      "uploaded": True
    }

    x = mycol.insert_one(single_project)
    return x.inserted_id

  def return_all_records(self):
    client = pymongo.MongoClient(self.url)
    mydb = client["universitas_library"]
    mycol = mydb["projects"]
    collection = []
    for record in mycol.find():
      collection.append(record)
    return json.dumps(collection, default=json_util.default)