from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
#from marshmallow_sqlalchemy import ModelSchema
#from marshmallow import fields



DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

def main():
    app.run()
    
    
if __name__ == '__main__':
    main()
    
