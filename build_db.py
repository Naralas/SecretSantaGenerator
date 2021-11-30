import os
from config import db
from models.list import *
from models.gift_relation import *

# Data to initialize database with
lists = [
    {'title':'MyList1', 'description':'This is the first list'},
    {'title':'MyList2', 'description':'This is the second list'},
]




# Delete database file if it exists currently
if os.path.exists("lists.db"):
    os.remove("lists.db")



# Create the database
db.drop_all()
db.create_all()

for l in lists:
    list_object = List(title=l['title'], description=l['description'])
    db.session.add(list_object)


db.session.commit()

lists = List.query.all()

relations = [
    GiftRelation(giver='Bob', receiver='Jean', list_id=lists[0].id),
    GiftRelation(giver='Jack', receiver='Amara', list_id=lists[0].id),
    GiftRelation(giver='Paul', receiver='Bob', list_id=lists[0].id),
    GiftRelation(giver='Amara', receiver='Paul', list_id=lists[0].id),
    GiftRelation(giver='Person1', receiver='Person3', list_id=lists[1].id),
    GiftRelation(giver='Person3', receiver='Person4', list_id=lists[1].id),
    GiftRelation(giver='Person2', receiver='Person1', list_id=lists[1].id),
    GiftRelation(giver='Person4', receiver='Person2', list_id=lists[1].id),   
]

db.session.add_all(relations)
db.session.commit()

list_schema = ListSchema()
dump_data = list_schema.dump(lists[0])
print(dump_data)