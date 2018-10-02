import pytest
from app.db import db
from app.models.models import User

def test_config(app):
    assert app.config['TESTING'] == True

def test_encode_auth_token(app):
    with app.app_context():
        user = User.create(email="test@test.pl",password="test")
        auth_token = user.encode_auth_token(user.id)
        assert isinstance(auth_token, bytes)

def test_decode_auth_token(app):
    with app.app_context():
        user = User.create(email="test@test.pl",password="test")
        auth_token = user.encode_auth_token(user.uuid)
        assert isinstance(auth_token, bytes)
        assert User.decode_auth_token(auth_token) == str(user.uuid)


