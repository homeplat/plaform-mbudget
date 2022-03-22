from flask import Blueprint
from flask_restful import Api

from app.dummy.api_v1 import init_api_v1_routes

dummy_v1_bp = Blueprint('dummy_v1_bp', __name__, url_prefix='/api/v1')

init_api_v1_routes(dummy_v1_bp)