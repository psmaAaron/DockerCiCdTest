import json

from flask import Blueprint
from mongo_db import mongo

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/')
def welcome_api():
    return "Welcome to the api!4444"

@api_bp.route('/getPoints')
def get_points():
  result = []
  for x in mongo.db.points.find({}, {'_id': False}):
    print(x)
    result.append(x)
  return json.dumps(result)
 

@api_bp.route('/add_point')
def add_point():
  sample_geojson_point = {
      "type": "Feature",
      "properties": {
        "dttm": 1548968278,
        "user": "Aaron",
        "message": "Dynamic Single Point Test"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          149.1441786289215,
          -35.321393219330126
        ]
      }
    }
    
  mongo.db.points.insert_one(sample_geojson_point)

  return('{"message" : "ok!"}')
