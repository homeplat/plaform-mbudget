from mimetypes import init
from multiprocessing.pool import INIT
from flask import Response, request
from flask_restful import Resource

from app.transactions.models import Transaction
from app.transactions.api_v1.schemas import transaction_schema

class TransactionsApi(Resource):
    def __init__(self, type) -> None:
        self.type = type
    
    def post(self):
        raw_data = request.get_json()
        raw_data['type'] = self.type
        data = transaction_schema.load(raw_data)
        # transaction = Transaction(**data).save()
        return Response(data, mimetype="application/json", status=201)
    
class IncomeApi(TransactionsApi):
    def __init__(self) -> None:
        super().__init__('income')