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
    #with open('data.JSON') as json_file:
     #   data = json.load(json_file) 
    #return  jsonify(data),200
    cursor = myDb.cursor()
    cursor.execute("SELECT * from Users")
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/image', methods=['POST'])
def compute():
    image = request.get_json()
    dict_image = dict(image)
    myDb = MYSQL.connect(host="147.232.40.14", user="km863qc", passwd="km863qc", database="km863qc", port=3306)
    cursor = myDb.cursor()
    cursor.execute("INSERT INTO Nakup (Nakup) VALUES ('{}')".format(data_dict['image']))
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("Created"),201