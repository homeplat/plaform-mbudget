""" All test related to dummy """
    
def test_dummy_endpoint(client):
        """
        GIVEN a flask application configured for testing
        WHERN the '/api/v1/dummy' endpoint is called with a GET method
        THEN check the response is successful and return a json with name property equal to 'Dummy'
        """
        response = client.get('/api/v1/dummy')
        assert response.status_code == 200
        assert response.json["name"] == "Dummy"
        