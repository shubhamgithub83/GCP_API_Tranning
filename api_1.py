from flask import Flask,jsonify, request
from flask_restful import Resource, Api
import json
app = Flask(__name__)

api = Api(app)
@app.route('/addage',methods=['POST'])
def addage():
     data = request.get_json()
     age=data["age"]
     random_no = data["random_no"]
     sum=age + random_no
     return jsonify(sum)


if __name__=='__main__':

    app.run(debug = True,host='127.0.0.1',port=5001)