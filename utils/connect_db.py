import os
import pymongo
import datetime
import dns # required for connecting with SRV

username = os.environ["MONGO_USER"]
password = os.environ["MONGO_PASS"]
url = "mongodb+srv://{}:{}@cluster0-rpoft.gcp.mongodb.net/test?retryWrites=true".format(username, password)

class Datastore:
  def __init__(self):
    username = os.environ["MONGO_USER"]
    password = os.environ["MONGO_PASS"]
    self.url = "mongodb+srv://{}:{}@cluster0-rpoft.gcp.mongodb.net/test?retryWrites=true".format(username, password)

  def insert_record(self, name, description, uploaded=True):
    client = pymongo.MongoClient(self.url)
    mydb = client["universitas_library"]
    mycol = mydb["projects"]

    single_project = {"createdAt": datetime.datetime.now(), "name": name, "description": description, "uploaded": True},

    x = mycol.insert_one(single_project)
    return x.inserted_id

  def return_all_records(self):
    client = pymongo.MongoClient(self.url)
    mydb = client["universitas_library"]
    mycol = mydb["projects"]
    collection = []
    for x in mycol.find():
      collection.append(x)
    return collection