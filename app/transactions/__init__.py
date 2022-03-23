from sys import prefix
from flask import Blueprint

from app.transactions.api_v1 import init_api_v1_routes

transactions_v1_bp = Blueprint('transaction_v1_bp', __name__, url_prefix='/api/v1/transactions')

init_api_v1_routes(transactions_v1_bp)