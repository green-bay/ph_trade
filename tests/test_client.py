import pytest
import json
import time

# helper functions
def _register_user(app, email, password):
    with app.test_client() as client:
        return client.post(
            '/api/register',
             data = json.dumps({
                    'email': email,
                    'password': password 
              }),
              content_type = 'application/json'
        )

def _login_user(app, email, password, return_token=False):
    with app.test_client() as client:
        response =  client.post(
                '/api/login',
                data = json.dumps({
                    'email': email,
                    'password': password
                }),
                content_type = 'application/json'
        )
        if return_token:
            data = json.loads(response.data.decode())
            return data.get('auth_token')
        return response

def _get_user_status(app, bearer):
    with app.test_client() as client:
        return client.get(
             '/api/login',
             headers = dict(Authorization=bearer)
        )

def _logout_user(app, bearer):
    with app.test_client() as client:
        return client.post(
             '/api/logout',
             headers = dict(Authorization=bearer)
        )

# helper functions end

test_email = 'test@email.com'
test_passw = 'test1234'
def test_registration(app):
    response = _register_user(app, test_email, test_passw)
    data = json.loads(response.data.decode())
    assert len(data.get('auth_token', '')) > 0
    assert response.content_type == 'application/json'
    assert response.status_code == 201

def test_register_existing_user(app):
    _register_user(app, test_email, test_passw)
    response = _register_user(app, test_email, test_passw)
    assert response.status_code == 202
    assert response.content_type == 'application/json'

def test_login_user(app):
    _register_user(app, test_email, test_passw)
    response = _login_user(app, test_email, test_passw)
    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert len(data.get('auth_token', '')) > 0
    assert response.content_type == 'application/json'

def test_login_bad_credentials(app):
    _register_user(app, test_email, test_passw)
    response = _login_user(app, test_email, 'wrongpass')
    data = json.loads(response.data.decode())
    assert len(data.get('auth_token', '')) == 0
    assert response.content_type == 'application/json'
    assert response.status_code == 404

def test_user_status(app):
    _register_user(app, test_email, test_passw)
    auth_token = _login_user(app, test_email, test_passw, True)
    response = _get_user_status(app, 'Bearer: %s' % auth_token) 
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert data.get('data', None) is not None
    assert data['data'].get('email') == test_email
    assert type(data['data'].get('admin')) == bool

def test_token_expierd(app):
    _register_user(app, test_email, test_passw)
    auth_token = _login_user(app, test_email, test_passw, True)
    time.sleep(6)
    response = _get_user_status(app, 'Bearer: %s' % auth_token) 
    data = json.loads(response.data.decode())
    assert response.status_code == 401

def test_user_logout(app):
    _register_user(app, test_email, test_passw)
    auth_token = _login_user(app, test_email, test_passw, True)
    bearer = 'Bearer: %s' % auth_token
    response = _get_user_status(app, bearer) 
    assert response.status_code == 200
    response = _logout_user(app, bearer)
    assert response.status_code == 200
    response = _get_user_status(app, bearer) 
    assert response.status_code == 401
