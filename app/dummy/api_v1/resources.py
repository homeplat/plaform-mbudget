from flask import Response
from flask_restful import Resource

class DummyApi(Resource):
    def get(self):
        return {"name": "Dummy"}, 200
