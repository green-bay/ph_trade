import pytest
from app import app

@pytest.fixture(scope="module")
def client():
    app.config.from_object('app.config.ConfigTest')
    return app.test_client()

def test_config(client):
    assert app.config['DEBUG'] == True
