import pytest
from app.db import db
from app.models.models import User
import json

def test_config(app):
    assert app.config['TESTING'] == True

def test_encode_auth_token(app):
    with app.app_context():
        user = User(email="test@test.pl",password="test")
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        assert isinstance(auth_token, bytes)

def test_decode_auth_token(app):
    with app.app_context():
        user = User(email="test@test.pl",password="test")
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        assert isinstance(auth_token, bytes)
        assert User.decode_auth_token(auth_token) == 1

def test_registration(app):
    with app.test_client() as client:
        response = client.post(
                '/api/register',
                data = json.dumps({
                    'email': 'john@doe.eo',
                    'password': 'johhny'
                }),
                content_type = 'application/json'
        )
        data = json.loads(response.data.decode())
        assert len(data.get('auth_token', '')) > 0
        assert response.content_type == 'application/json'
        assert response.status_code == 201

def test_register_existing_user(app):
    with app.test_client() as client:
        email = 'test@test.pl'
        password = 'test'
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        response = client.post(
                '/api/register',
                data = json.dumps({
                    'email': email,
                    'password': password
                }),
                content_type = 'application/json'
        )
        assert response.status_code == 202
        assert response.content_type == 'application/json'

def test_login_user(app):
    with app.test_client() as client:
        email = 'test@test.pl'
        password = 'test'
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        response = client.post(
                '/api/login',
                data = json.dumps({
                    'email': email,
                    'password': password
                }),
                content_type = 'application/json'
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert len(data.get('auth_token', '')) > 0
        assert response.content_type == 'application/json'

def test_login_bad_credentials(app):
    with app.test_client() as client:
        email = 'test@test.pl'
        password = 'test'
        response = client.post(
                '/api/login',
                data = json.dumps({
                    'email': email,
                    'password': password
                }),
                content_type = 'application/json'
        )
        data = json.loads(response.data.decode())
        assert len(data.get('auth_token', '')) == 0
        assert response.content_type == 'application/json'
        assert response.status_code == 404

