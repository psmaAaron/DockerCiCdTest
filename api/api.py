import json

from flask import Blueprint, request
from mongo_db import mongo

import time

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/')
def welcome_api():
    return "Welcome to the api!"

@api_bp.route('/point', methods=['GET','POST'])
def point():
  if  request.method == 'GET':
    return get_points()
  elif request.method == 'POST':
    return add_point()
  else:
    return 

def get_points():
  result = []
  for x in mongo.db.points.find({}, {'_id': False}):
    result.append(x)
  return json.dumps(result)
 
def add_point():
  json_req = request.get_json()

  sample_geojson_point = {
      "type": "Feature",
      "properties": {
        "dttm": int(time.time()),
        "user": "Dynamic",
        "message": "Dynamic"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          json_req['lng'],
          json_req['lat']
        ]
      }
    }
    
  mongo.db.points.insert_one(sample_geojson_point)

  return('{"message" : "ok!"}')
