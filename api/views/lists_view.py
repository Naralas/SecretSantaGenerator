from flask import request, jsonify
from flask_restful import Resource
from models.list import List, ListSchema

class MultiListResource(Resource):
    multi_list_schema = ListSchema(many=True)
    def get(self):
        
        all_lists = List.query.all()
        return self.multi_list_schema.dump(all_lists)
        
    def post(self):
        pass

class SingleListResource(Resource):
    single_list_schema = ListSchema()
    def get(self, id):
        selected_list = List.query.get(id)
        return self.single_list_schema.dump(selected_list)
    
    def put(self):
        pass
    
    def delete(self):
        pass

    
    