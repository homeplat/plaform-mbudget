from flask import Flask
from flask_restful import Api

from app.dummy import dummy_v1_bp

def create_app():
    # Instance Flask app
    app = Flask(__name__)
    api = Api(app)
    
    app.register_blueprint(dummy_v1_bp)
    
    return app