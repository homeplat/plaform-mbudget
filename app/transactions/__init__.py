from sys import prefix
from flask import Blueprint, Flask

from app.transactions.api_v1 import init_api_v1_routes

transactions_v1_bp = Blueprint('transaction_v1_bp', __name__, url_prefix='/api/v1/transaction')

init_api_v1_routes(transactions_v1_bp)

def register_transactions(app: Flask):
    app.register_blueprint(transactions_v1_bp)