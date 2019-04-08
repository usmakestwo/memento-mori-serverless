from flask import jsonify
from utils.connect_db import Datastore
from utils.connect_github import GithubClient

# Databases
db = Datastore()
git = GithubClient()

def create_project(request):
  if request.is_json:
    content = request.get_json()
    git_response = git.createRepo(content['name'], content['description'])
    if git_response:
      db.insert_record(content['name'], content['description'], git_response)
      response = jsonify(text='Project successfully created'), 200
      return response
    else:
      response = jsonify(text='Failed creating project'), 400
      return response
  else:
    response = jsonify(text='Not valid JSON'), 400
    return response