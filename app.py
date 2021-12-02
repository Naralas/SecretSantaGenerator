from flask import Flask, request, jsonify, make_response
from flask import render_template

from extensions import db, ma, api
from views.lists_view import MultiListResource, SingleListResource
from flask_restful import Api

import config

# structure inspired by https://github.com/cookiecutter-flask/cookiecutter-flask

def setup_routes(api):
    api.add_resource(SingleListResource, '/List/<string:id>')
    api.add_resource(MultiListResource, '/List/')

def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
        
    setup_routes(api)
    api.init_app(app)
    

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)

    return app
    
if __name__ == "__main__":
    app = create_app(config)
    app.run(debug=True)
