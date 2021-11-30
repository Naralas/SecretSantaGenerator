from config import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from models.gift_relation import GiftRelationSchema

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(200))
    
    gifts = db.relationship('GiftRelation', backref='list', lazy=True)
    

class ListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = List
        load_instance = True
        include_relationships = True
        
    books = fields.Nested(GiftRelationSchema, many=True)