"""
REST API resource routing
part of flask-restplus
"""

from datetime import datetime
from flask import request, current_app
from flask_restplus import Resource, abort, marshal, fields
from flask_login import current_user, login_user, logout_user
from app.models.users import User
from app.models.classifieds import ClassifiedAd, ClassifiedTags

from .security import require_auth
from . import api_rest
from app.db import db,bcrypt
import uuid

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]



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
            login_user(user, remember=False)
            return {'user_name': user.email}, 201
        else:
            return abort(404)

    def get(self):
        if current_user.is_authenticated:
            return {'message': 'User logged in'}, 202
        else:
            return {}, 200

@api_rest.route('/user/is_authenticated')
class UserAuthenticated(SecureResource):
    def get(self):
        return {}, 200


@api_rest.route('/user/status')
class UserStatus(SecureResource):
    def get(self, user):
        """Get user status"""
        return dict(data=dict(email=user.email, admin=user.admin)), 200

        
@api_rest.route('/logout')
class LogoutUser(SecureResource):
    def get(self):
        logout_user()
        return {}, 200

cat_fields = {
    'id': fields.Raw,
    'name': fields.String
}

user_fields = {
    'id': fields.Raw,
    'name': fields.String(attribute='email'),
    'mail': fields.String(attribute='email'),
    'password': fields.String
}

ads_fields = {
    'id': fields.Raw,
    'name': fields.String,
    'categories': fields.Nested(cat_fields),
    'phone': fields.String,
    'email': fields.String,
    'description': fields.String
}

@api_rest.route('/models/<model>')
class GetModel(SecureResource):
    def get(self, model):
        models = {'ads': (ClassifiedAd, ads_fields), 
                'categories': (ClassifiedTags, cat_fields),
                'users': (User, user_fields)}
        if not model in models:
            return abort(404)
        db_model, model_fields = models[model]
        return {'content': marshal(db_model.query.all(), model_fields),
                'headers': list(model_fields.keys())}, 200

@api_rest.route('/ads')
class ClassifiedAds(Resource):

    def get(self):
        res = marshal(ClassifiedAd.get_all(), ads_fields)
        return res, 200

    def post(self):
        post = request.json
        categories = post.pop('categories')
        tags = ClassifiedTags.query.filter(ClassifiedTags.name.in_(categories)).all()
        post['categories'] = tags
        ad = ClassifiedAd.create(**post)
        return marshal(ad, ads_fields), 201
    
@api_rest.route('/ad/attrs')
class ClasssifiedAdsAttrs(Resource):
    
    def get(self):
        return {'cats': marshal(ClassifiedTags.get_all(), cat_fields)}, 200
    
    def post(self):
        post = request.json
        attr = ClassifiedTags.create(**post)
        return marshal(attr, cat_fields), 201


