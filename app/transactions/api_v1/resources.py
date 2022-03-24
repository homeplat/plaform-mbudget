from email import message
from http.client import BAD_REQUEST
from mimetypes import init

from marshmallow.exceptions import ValidationError
from flask import Response, request
from flask_restful import Resource, abort

from app.transactions.api_v1.schemas import transaction_schema

class TransactionsApi(Resource):
    def __init__(self, type) -> None:
        self.type = type
    
    def post(self):
        raw_data = request.get_json()
        raw_data['type'] = self.type
        data = transaction_schema.load(raw_data)
        data.save()
        return transaction_schema.dump(data), 201
        
    
class IncomeApi(TransactionsApi):
    def __init__(self) -> None:
        super().__init__('income')