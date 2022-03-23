""" Tests related to transaction CRUD """
import json

base_income_url = "/api/v1/transactions/income"

def test_transaction_creation_income(client):
    """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/transaction/income' endpoint is called with a POST method and valid json as body
        THEN check the response is created(201) and return a json with the transaction created with id
    """
    data = json.dumps({
        'amount': 12000,
        'date': '2022-03-25'
    })
    response = client.post(
        base_income_url,
        headers={'Content-Type': 'application/json'},
        data=data
    )
    
    assert response.status_code == 201
    assert response.json["id"] != ''
    