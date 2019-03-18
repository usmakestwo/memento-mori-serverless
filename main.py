from flask import Flask, Response, request, jsonify
from utils.connect_db import Datastore
from utils.connect_github import GithubClient

# Databases
db = Datastore()
git = GithubClient()

# Initialize Flask
app = Flask(__name__)

@app.route("/health")
def health():
  return 'OK'

@app.route("/api/projects")
def fetchProjects():
  projects = db.return_all_records()
  return Response(projects, status=200, mimetype='application/json')

@app.route("/api/project", methods = ['POST'])
def createProject():
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

