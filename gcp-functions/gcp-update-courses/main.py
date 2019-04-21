from flask import jsonify
from utils.connect_db import Datastore

# Databases
db = Datastore()

def update_project(request):
  if request.is_json:
    content = request.get_json()
    result = db.update_record(content['name'], content['status'])
    if result:
      response = jsonify(text='Project updated'), 200
    else:
      response = jsonify(text='Project not found'), 400
    return response
  else:
    response = jsonify(text='Not valid JSON'), 400
    return response