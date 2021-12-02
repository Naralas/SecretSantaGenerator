from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Create the SQLAlchemy db instance
db = SQLAlchemy()

# Initialize Marshmallow
ma = Marshmallow()

# set the routes
api = Api()