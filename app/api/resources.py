"""
REST API resource routing
part of flask-restplus
"""

from datetime import datetime
from flask import request, current_app
from flask_restplus import Resource, abort
from app.models.models import User

from .security import require_auth
from . import api_rest
from app.db import db,bcrypt
import uuid

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]

ADS = [
    {
        'name': 'nasiona',
        'category': 'różne',
        'desc': 'mam do sprzedania 1kg nasion',
        'publisher': 'Dr Green Thumb',
        'image': 'https://zielonaesencja.pl/pol_pm_Szalwia-Hiszpanska-BIO-Nasiona-Chia-1-kg-BIO-PLANET-1434_3.jpg'
    },
    {
        'name': 'susz',
        'category': 'inne',
        'desc': 'sprzedam susz',
        'publisher': 'Snoop Dog',
        'image': 'https://hempyourself.store/userdata/gfx/3a3a93d8a1dc3b81e132b6a8ca77ad1d.jpg'
    }
        ]

@api_rest.route('/ads')
class ClassifiedAds(Resource):

    def get(self):
        return ADS

    def post(self):
        post = request.json
        ADS.append({
            'name': post.get('name'),
            'category': post.get('category'),
            'desc': post.get('desc'),
            'publisher': post.get('publisher'),
            'image': post.get('image')
        })
        return ADS[-1], 201


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

@api_rest.route('/register')
class RegisterUser(Resource):
    def post(self):
        post_data = request.get_json()
        email = post_data.get('email')
        user = User.query.filter_by(email=email).first()
        if not user:
            try:
                user = User.create(
                    email=email,
                    password=post_data.get('password')
                )
                auth_token = user.encode_auth_token(user.uuid)
                return {'auth_token': auth_token.decode()}, 201
            except Exception as e:
                return abort(401, str(e))
        else:
            return {'message': 'User exists'}, 202

@api_rest.route('/login')
class LoginUser(Resource):
    def post(self):
        post_data = request.get_json()
        user = User.query.filter_by(email=post_data.get('email')).first()
        if user and bcrypt.check_password_hash(user.password, post_data.get('password')):
            auth_token = user.encode_auth_token(user.uuid)
            if auth_token:
                return {'auth_token': auth_token.decode()}, 201
        else:
            return abort(404)

@api_rest.route('/user/status')
class UserStatus(SecureResource):
    def get(self, user):
        """Get user status"""
        return dict(data=dict(email=user.email, admin=user.admin)), 200

        
@api_rest.route('/logout')
class LogoutUser(SecureResource):
    def post(self, user):
        user.write(uuid = uuid.uuid1())
        return {}, 200
