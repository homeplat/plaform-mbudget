""" Tests related to transaction CRUD """
import datetime
import json
import pytest

from mongoengine.errors import DoesNotExist

from app.transactions.models import Transaction
from app.transactions.api_v1.schemas import transaction_schema

base_url = "/api/v1/transaction"

def test_transaction_get_list(client):
    """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/transaction' endpoint is called with a GET method
        THEN check the response is OK(200) and return a json with a list of transactions
    """
    array = [
        {'amount': 1000000, 'type': 'income', 'date': '2022-03-26'},
        {'amount': 500000, 'type': 'income', 'date': '2022-03-26'},
        {'amount': 250000, 'type': 'expense', 'date': '2022-03-25'},
        {'amount': 100000, 'type': 'income', 'date': '2022-03-25'},
        {'amount': 1200000, 'type': 'expense', 'date': '2022-03-24'}
    ]
    transactions = [Transaction(**data) for data in array]
    Transaction.objects.insert(transactions, load_bulk=False)
    
    response = client.get(base_url)
    
    assert response.status_code == 200
    assert len(response.json) == len(array)  

def test_transaction_creation(client):
    """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/transaction' endpoint is called with a POST method and valid json as body
        THEN check the response is CREATED(201) and return a json with the transaction created with id
    """
    data = json.dumps({
        'amount': 12000,
        'type': 'income',
        'date': '2022-03-25'
    })
    response = client.post(
        base_url,
        headers={'Content-Type': 'application/json'},
        data=data
    )
    
    assert response.status_code == 201
    assert response.json["id"] != ''
    assert response.json["amount"] == 12000
    assert response.json["type"] == 'income'
    assert response.json["date"] == '2022-03-25'
    assert response.json["creation_date"] != ''
    
def test_transaction_creation_invalid_input(client):
    """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/transaction' endpoint is called with a POST method and invalid json as body
        THEN check the response is BAD REQUEST(400) and return a json with the errors
    """
    data = json.dumps({
        'amount': -12000,   # Cannot be negative
        'type': 'wrong',   # Must be income or expense
        'date': '2022/03/25' # Invalid format
    })
    response = client.post(
        base_url,
        headers={'Content-Type': 'application/json'},
        data=data
    )
    
    assert response.status_code == 400
    assert response.json["error"]["type"][0] == 'Must be one of: income, expense.'
    assert response.json["error"]["date"][0] == 'Not a valid datetime.'
    assert response.json["error"]["amount"][0] == 'Must be greater than or equal to 1.'
    
def test_transaction_creation_missing_required(client):
    """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/transaction' endpoint is called with a POST method and missing fiels in b  json as body
        THEN check the response is BAD REQUEST(400) and return a json with the errors
    """
    data = json.dumps({
    })
    response = client.post(
        base_url,
        headers={'Content-Type': 'application/json'},
        data=data
    )
    
    assert response.status_code == 400
    assert response.json["error"]["date"][0] == 'Missing data for required field.'
    assert response.json["error"]["amount"][0] == 'Missing data for required field.'
    assert response.json["error"]["type"][0] == 'Missing data for required field.'
    
def test_transaction_delete_existing(client):
    """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/transaction/<id>' endpoint is called with a DELETE method
        THEN check the response is NO CONTENT(204)
    """
    # Create data to delete
    data = Transaction(**{
        'amount': 12000,
        'type': 'income',
        'date': '2022-03-25'
    }).save()
    
    response = client.delete(f'{base_url}/{data.id}')
    
    assert response.status_code == 204
    
    with pytest.raises(DoesNotExist):
        Transaction.objects.get(id=data.id)
        
def test_transaction_delete_not_existing(client):
    """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/transaction/<id>' endpoint is called with a DELETE method
        THEN check the response is NOT FOUND(404)
    """
    id = '623d3e81a77ac1c30ba367fa'
    response = client.delete(f'{base_url}/{id}')
    
    assert response.status_code == 404
    assert response.json["error"] == f'Transaction with id {id} does not exist.'
    
def test_transaction_update(client):
    """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/transaction/<id>' endpoint is called with a PUT method and valid json as body
        THEN check the response is OK(200) and return a json with the transaction updated.
    """
    transaction = Transaction(**{
        'amount': 12000,
        'type': 'income',
        'date': '2022-03-25'
    }).save()
    
    data = json.dumps({
        'amount': 1500,
        'type': 'expense',
        'date': '2022-03-27'
    })
    response = client.put(
        f'{base_url}/{transaction.id}',
        headers={'Content-Type': 'application/json'},
        data=data
    )
    
    assert response.status_code == 200
    assert response.json["id"] == str(transaction.id)
    assert response.json["amount"] == 1500
    assert response.json["type"] == 'expense'
    assert response.json["date"] == '2022-03-27'