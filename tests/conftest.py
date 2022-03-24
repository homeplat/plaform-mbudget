import os
from app import create_app
import pytest

@pytest.fixture()
def app():
    os.environ["FLASK_ENV"] = "testing"
    
    app = create_app()

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()