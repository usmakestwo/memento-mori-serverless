import flask
from utils.connect_db import Datastore

# Databases
db = Datastore()

def update_project(request):
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
    result = db.update_record(content['id'], content['source'], content['target'])
    if result:
      resp = flask.Response(response="Project Updated", status=200, headers=headers)
      return resp
    else:
      resp = flask.Response(response="Project not found", status=404, headers=headers)
      return resp
  else:
    resp = flask.Response(response="Not valid JSON", status=400, headers=headers)
    return resp