from app.db import db

class Transaction(db.Document):
    amount = db.IntField(required=True)
    date = db.DateTimeField(required=True)
    type = db.StringField(required=True)
    creationDate = db.DateTimeField()