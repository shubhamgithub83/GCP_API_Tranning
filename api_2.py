from flask import Flask,jsonify, request
from flask_restful import Resource, Api
import json
app = Flask(__name__)

api = Api(app)
@app.route('/sumby2',methods=['POST'])
def sumby2():
     data = request.get_json()
     ans=int(data["sum"])
     ans=ans/2
     return jsonify(ans)

if __name__=='__main__':

    app.run(debug = True,host='127.0.0.1',port=5002)