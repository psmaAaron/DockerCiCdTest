import json

from flask import Flask
 
app = Flask(__name__)

@app.route('/api')
def welcome_api():
    return "Welcome to the api!"

@app.route('/api/getPoints')
def get_points():
    sample_geojson_point = {
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
    }

    return json.dumps(sample_geojson_point)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
