from flask import jsonify
from utils.connect_db import Datastore
from utils.connect_github import GithubClient

# Databases
db = Datastore()
git = GithubClient()

def create_project(request):
  response.headers.set('Access-Control-Allow-Origin', '*')
  response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
  if request.is_json:
    content = request.get_json()
    response = git.createRepo(content['name'], content['description'])
    if response:
      db.insert_record(content['name'], content['description'])
      response = jsonify(text='Project successfully created'), 200
      response.headers.set('Access-Control-Allow-Origin', '*')
      response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
      return response
    else:
      response = jsonify(text='Failed creating project'), 400
      response.headers.set('Access-Control-Allow-Origin', '*')
      response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
      return response
  else:
    response = jsonify(text='Not valid JSON'), 400
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response