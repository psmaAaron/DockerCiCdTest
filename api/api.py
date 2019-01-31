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
          149.1441786289215,
          -35.321393219330126
        ]
      }
    }]

    return json.dumps(sample_geojson_point)
 
