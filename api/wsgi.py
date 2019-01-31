from flask import Flask
from api import api_bp

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    app.run()
    