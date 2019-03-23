from flask import jsonify
from utils.connect_db import Datastore
from utils.connect_github import GithubClient

# Databases
db = Datastore()
git = GithubClient()

def create_project(request):
  if request.is_json:
    content = request.get_json()
    response = git.createRepo(content['name'], content['description'])
    if response:
      db.insert_record(content['name'], content['description'])
      return 'Project successfully created'
    else:
      return jsonify(text='Failed creating project'), 400
  else:
    return 'Not Valid JSON'
  content = request.get_json()
  print (content)
  return 'JSON posted'