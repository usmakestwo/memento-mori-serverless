import flask
from utils.connect_db import Datastore
from utils.connect_github import GithubClient

# Databases
db = Datastore()
git = GithubClient()

def create_project(request):
  # Set CORS headers for the preflight request
  if request.method == 'OPTIONS':
    # Allows POST requests from any origin with the Content-Type
    # header and caches preflight response for an 3600s
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600'
    }

    return ('', 204, headers)

  # Set CORS headers for the main request
  headers = {
      'Access-Control-Allow-Origin': '*'
  }

  if request.is_json:
    content = request.get_json()
    git_response = git.createRepo(content['name'], content['description'])
    if git_response:
      db.insert_record(content['name'], content['description'], git_response)
      resp = flask.Response(response="Project successfully created", status=200, headers=headers)
      return resp
    else:
      resp = flask.Response(response="Failed creating project", status=404, headers=headers)
      return resp
  else:
    resp = flask.Response(response="Not valid JSON", status=400, headers=headers)
    return resp