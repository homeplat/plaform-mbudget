from flask import Flask
from flask_restful import Api

# from app.db import db
from app.ext import ma

from app.dummy import dummy_v1_bp
from app.transactions import transactions_v1_bp

def create_app():
    # Instance Flask app
    app = Flask(__name__)
    api = Api(app)
    
    # db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(dummy_v1_bp)
    app.register_blueprint(transactions_v1_bp)
    
    return app