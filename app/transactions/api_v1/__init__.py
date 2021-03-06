from flask import Blueprint
from flask_restful import Api

from app.transactions.api_v1.resources import TransactionsApi

def init_api_v1_routes(blueprint):
    api = Api(blueprint)
    
    api.add_resource(TransactionsApi, '/', '/<id>')