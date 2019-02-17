from flask import Flask
from api import api_bp
from mongo_db import mongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/testdb"
mongo.init_app(app)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')