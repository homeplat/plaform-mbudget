import os

from flask import Flask
from flask_restful import Api

from app.db import db
from app.ext import ma
from app.common.error_handling import register_error_handlers

from app.transactions import register_transactions

def create_app():
    # Instance Flask app
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    # Config Flask application
    init_from_config(app)
    api = Api(app, catch_all_404s=True)
    
    db.init_app(app) # initialize mongodb
    ma.init_app(app)
    
    register_transactions(app)
    register_error_handlers(app)
    
    return app

def init_from_config(app: Flask):
    # Configuration loaded from config file
    app.config.from_object('config.default')
    # Configuration loaded from config file in instance folder
    app.config.from_pyfile('config.py')
    
    env = os.environ.get('FLASK_ENV', default='production')
    app.config.from_object(f'config.{env}')