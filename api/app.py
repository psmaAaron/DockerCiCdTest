from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the api."

@app.route('/api')
def welcome_api():
    return "Welcome to the api. THROUGH API!"
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
