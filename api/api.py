import json
from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/')
def welcome_api():
    return "Welcome to the api!"

@api_bp.route('/getPoints')
def get_points():
    sample_geojson_point = [{
      "type": "Feature",
      "properties": {
        "dttm": 1548968278,
        "user": "Aaron",
        "message": "Single Point Test"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          125.5078125,
          58.26328705248601
        ]
      }
    }]

    return json.dumps(sample_geojson_point)
 
