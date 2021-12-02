from extensions import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

    
class GiftRelation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    giver = db.Column(db.String(30))
    receiver = db.Column(db.String(30))
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
    
    
    def __repr__(self):
        return f"{giver} -> {receiver}"


class GiftRelationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GiftRelation
        load_instance = True