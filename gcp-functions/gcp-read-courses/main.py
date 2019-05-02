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
  kanban = mydb["kanban"]
  projects = mydb["projects"]
  collection = []

  for x in kanban.find():
    collection.append(x)

  # Store each card reference from kanban project
  for x in kanban.find({ "id": "wip" }):
    wip_projects = x['cards']

  for x in kanban.find({ "id": "learned" }):
    learned_projects = x['cards']

  for x in kanban.find({ "id": "backlog" }):
    backlog_projects = x['cards']

  for x in kanban.find({ "id": "practice" }):
    practice_projects = x['cards']

  wip_projects = list(projects.find({"_id": {"$in": wip_projects }}))
  learned_projects = list(projects.find({"_id": {"$in": learned_projects }}))
  backlog_projects = list(projects.find({"_id": {"$in": backlog_projects }}))
  practice_projects = list(projects.find({"_id": {"$in": practice_projects }}))

  for item in range(len(collection)):
    if collection[item]["id"] == "backlog":
      collection[item]["cards"] = backlog_projects
    elif collection[item]["id"] == "wip":
      collection[item]["cards"] = wip_projects
    elif collection[item]["id"] == "learned":
      collection[item]["cards"] = learned_projects
    elif collection[item]["id"] == "practice":
      collection[item]["cards"] = practice_projects

  response = jsonify(json.dumps(collection, default=json_util.default))
  response.headers.set('Access-Control-Allow-Origin', '*')
  response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
  return response