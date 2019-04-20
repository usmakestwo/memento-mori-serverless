import os
import pymongo
import datetime
import json
from flask import jsonify
from bson import json_util

def return_all_records(request):
  username = os.environ["MONGO_USER"]
  password = os.environ["MONGO_PASS"]
  url = "mongodb://{}:{}@cluster0-shard-00-00-rpoft.gcp.mongodb.net:27017,cluster0-shard-00-01-rpoft.gcp.mongodb.net:27017,cluster0-shard-00-02-rpoft.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true".format(username, password)
  client = pymongo.MongoClient(url)
  mydb = client["universitas_library"]
  mycol = mydb["projects"]
  collection = []
  for record in mycol.find():
    collection.append(record)
  response = jsonify(json.dumps(collection, default=json_util.default))
  response.headers.set('Access-Control-Allow-Origin', '*')
  response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
  return response