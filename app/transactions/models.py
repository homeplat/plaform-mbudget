from datetime import datetime

from app.db import db

class Transaction(db.Document):
    amount = db.IntField(required=True, min_value=1)
    date = db.DateTimeField(required=True)
    type = db.StringField(required=True)
    creation_date = db.DateTimeField(default=datetime.utcnow)