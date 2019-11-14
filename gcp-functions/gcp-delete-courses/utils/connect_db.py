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
    self.client = pymongo.MongoClient(self.url)
    print("Connected with Database")

  def delete_single_record(self, id):
    mydb = self.client["universitas_library"]
    # kanban = mydb["kanban"]
    projects = mydb["projects"]

    try:
      x = projects.delete_one({"_id": objectid.ObjectId(id)})
      return x
    except Exception as e:
      print(e)
      return e

## TODO: Remove card from appropriate lane


# 5dcb15183b77500001dc9de8

# db.kanban.find({"cards": { $all:[ObjectId("5c8eaaa2246320a756ef64e0")] }})

# {
#   "_id": ObjectId("5ccab808d406c4c167215103"),
#   "id": "backlog",
#   "title": "Backlog",
#   "style": {
#     "width": 280
#   },
#   "cards": [ ObjectId("5c8eaaa2246320a756ef64e0"), ObjectId("5c8eaaa2246320a756ef64dc"), ObjectId("5c8eaaa2246320a756ef64dd"), ObjectId("5c8eaaa2246320a756ef64e2"), ObjectId("5c8eaaa2246320a756ef64e4"), ObjectId("5c8eaaa2246320a756ef64df"), ObjectId("5c8eaaa2246320a756ef64de"), ObjectId("5c8eaaa2246320a756ef64e1"), ObjectId("5c8eaaa2246320a756ef64e3"), ObjectId("5cb242ad3b77500001744070"), ObjectId("5cd4d6cc3b77500001eaffe8"), ObjectId("5c8eaaa2246320a756ef64d6"), ObjectId("5c8eaaa2246320a756ef64d7"), ObjectId("5cdca64c3b7750000161c753"), ObjectId("5cdcd3583b7750000161c755"), ObjectId("5c8eaaa2246320a756ef64d3"), ObjectId("5c8eaaa2246320a756ef64d5"), ObjectId("5cf853af3b77500001f42f7a"), ObjectId("5cf8f7783b77500001f42f7c"), ObjectId("5ce860c13b77500001771d47"), ObjectId("5c8eaaa2246320a756ef64d2"), ObjectId("5cde155a3b7750000161c757"), ObjectId("5da215483b77500001e27f8f"), ObjectId("5da218ac3b77500001e27f91"), ObjectId("5da219b73b77500001e27f93"), ObjectId("5c8eaaa2246320a756ef64db"), ObjectId("5c8eaaa2246320a756ef64d4"), ObjectId("5c8eaaa2246320a756ef64d8"), ObjectId("5dc444563b775000018f5dff"), ObjectId("5dc44b503b77500001dc9de6"), ObjectId("5dcb15183b77500001dc9de8")
#   ]
# }


# db.kanban.find({"cards": [ObjectId("5c8eaaa2246320a756ef64e0")] })

# db.inventory.find( { tags: { $all: ["red"] } } )

# db.kanban.find({ cards: ObjectId("5c8eaaa2246320a756ef64e0") } )