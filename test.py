#using flask_restful
from flask import Flask,jsonify, request
from flask_restful import Resource, Api
import json

#creating the flask app
app = Flask(__name__)
#creating an API object
api = Api(app)

#making a class for a particular resource
# the get , post methods correspond to get and post requests
#they are automatically mapped by flask_restful
# other methods include put, delete, etc.
class Hello(Resource):
    def get(self):
        return jsonify({'message':'Hello world'})

    def post(self):
        data = request.get_json()
        print(data['num'])
        num =data['num']
        return jsonify({'response':pow(int(num),3)})

class Square(Resource):

    def get(self, num):
        return jsonify({'square':num**2})

api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')

if __name__=='__main__':

    app.run(debug = True,host='0.0.0.0',port=5000)