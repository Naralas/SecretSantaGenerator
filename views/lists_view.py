from app import app
from flask import request, jsonify
from models.list import List

#https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

@app.route('/list', methods=['GET'])
def get_list():
    if 'id' in request.args:
        print(request['id'])
    else:
        return jsonify({'Error':'Id not provided'})