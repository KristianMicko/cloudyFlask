from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

@app.route('/', methods=['GET'])
def computing():
    with open('data.JSON') as json_file:
        data = json.load(json_file) 
    return  jsonify(data),200
