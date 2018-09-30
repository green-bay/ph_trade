"""
REST API resource routing
part of flask-restplus
"""

from datetime import datetime
from flask import request, current_app
from flask_restplus import Resource
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
                user = User(
                    email=email,
                    password=post_data.get('password')
                )
                db.session.add(user)
                db.session.commit()
                auth_token = user.encode_auth_token(user.uuid)
                return {'auth_token': auth_token.decode()}, 201
            except Exception as e:
                raise e
                return {'message': e.message}, 401
        else:
            return {}, 202 #user exists

@api_rest.route('/login')
class LoginUser(Resource):
    def post(self):
        post_data = request.get_json()
        try:
            user = User.query.filter_by(email=post_data.get('email')).first()
            if user and bcrypt.check_password_hash(user.password, post_data.get('password')):
                auth_token = user.encode_auth_token(user.uuid)
                if auth_token:
                    return {'auth_token': auth_token.decode()}, 201
            else:
                return {}, 404
        except Exception as e:
            current_app.logger.debug(str(e))
            return {'exception': str(e)}, 500 

    def get(self):
        """Get user status"""
        bearer = request.headers.get('Authorization')
        try:
            auth_token = bearer.split(" ")[1]
            uuid = User.decode_auth_token(auth_token)
            if uuid:
                user = User.query.filter_by(uuid=uuid).first()
                if user:
                    return dict(data=dict(email=user.email, admin=user.admin)), 200
                return {},401
            else:
                return {},401
        except Exception as e:
            return {}, 401 
        
@api_rest.route('/logout')
class LogoutUser(Resource):
    def post(self):
        bearer = request.headers.get('Authorization')
        try:
            auth_token = bearer.split(" ")[1]
            resp = User.decode_auth_token(auth_token)
            if resp:
                user = User.query.filter_by(uuid=resp).first()
                if user:
                    user.uuid = uuid.uuid1()
                    db.session.commit()
                    return {}, 200
                return {},401
            else:
                return {},401
        except Exception as e:
            current_app.logger.debug(str(e))
            return {}, 401 
