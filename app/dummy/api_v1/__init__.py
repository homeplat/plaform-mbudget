from ast import Import
from flask_restful import Api

from app.dummy.api_v1.resources import DummyApi

def init_api_v1_routes(blueprint):
    api = Api(blueprint)
    
    api.add_resource(DummyApi, '/dummy')