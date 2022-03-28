from datetime import datetime
from marshmallow import ValidationError

from marshmallow.validate import OneOf
from marshmallow_mongoengine import ModelSchema, fields

from app.transactions.models import Transaction

def date_val(d):
    try:
        d.strftime('%Y-%m-%d')
    except ValueError:
        raise ValidationError('Not valid date. Shoueld be YYYY-MM-DD.')

class TransactionSchema(ModelSchema):
    class Meta:
        model = Transaction
        model_fields_kwargs = {'date': {'format': '%Y-%m-%d'}}
    
    type = fields.String(required=True, validate=OneOf(['income', 'expense']))
    # date = fields.Date(required=True, validate=date_val)
        
transaction_schema = TransactionSchema()