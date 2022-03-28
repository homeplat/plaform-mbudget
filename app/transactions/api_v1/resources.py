from flask import request
from flask_restful import Resource, abort
from marshmallow.exceptions import ValidationError
from mongoengine.errors import DoesNotExist

from app.transactions.api_v1.schemas import transaction_schema
from app.transactions.models import Transaction

class TransactionsApi(Resource):
    # def __init__(self, type) -> None:
    #     self.type = type
    def get(self):
        data = Transaction.objects()
        return transaction_schema.dump(data, many=True), 200
    
    def post(self):
        try:
            raw_data = request.get_json()
            # raw_data['type'] = self.type
            data = transaction_schema.load(raw_data)
            data.save()
            return transaction_schema.dump(data), 201
        except ValidationError as e:
            abort(400, error=e.messages)
            
    def delete(self, id):
        try:
            data = Transaction.objects.get(id=id)
            data.delete()
            return {}, 204
        except DoesNotExist:
            abort(404, error=f'Transaction with id {id} does not exist.')
            
    def put(self, id):
        raw_data = request.get_json()
        data = Transaction.objects.get(id=id)
        data = transaction_schema.update(data, raw_data)
        data.save()
        return transaction_schema.dump(data), 200
        
        
    
# class IncomeApi(TransactionsApi):
#     def __init__(self) -> None:
#         super().__init__('income')