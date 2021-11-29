from config import db

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(200))
    
    gifts = db.relationship('GiftRelation', backref='list', lazy=True)
    
class GiftRelation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    giver = db.Column(db.String(30))
    receiver = db.Column(db.String(30))
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
    