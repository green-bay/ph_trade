import datetime
import jwt
from flask import current_app as app
from app.db import db, bcrypt
import uuid
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    uuid = db.Column(UUID(as_uuid=True), nullable=False, unique=True)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.admin = admin
        self.uuid = uuid.uuid1()

    def encode_auth_token(self, uuid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': str(uuid)
            }
            return jwt.encode(
                    payload, 
                    app.config.get('SECRET_KEY'), 
                    algorithm='HS256'
            )
        except Exception as e:
            raise e
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the Auth Token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(
                        auth_token, 
                        app.config.get('SECRET_KEY'),
                        algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Login again, please'
        except jwt.InvalidTokenError:
            return 'Token invalid. Login again, please'

