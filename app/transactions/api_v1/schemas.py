from marshmallow_mongoengine import ModelSchema

from app.transactions.models import Transaction

class TransactionSchema(ModelSchema):
    class Meta:
        model = Transaction
        model_fields_kwargs = {'date': {'format': '%Y-%m-%d'}}
        
transaction_schema = TransactionSchema()