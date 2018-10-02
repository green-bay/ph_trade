from functools import wraps
from flask import request, current_app
from flask_restplus import abort
from app.models.models import User


def require_auth(func):
    """Secure method decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.headers.get('Authorization'):
            bearer = request.headers.get('Authorization')
            try:
                auth_token = bearer.split(" ")[1]
                uuid = User.decode_auth_token(auth_token)
                if uuid:
                    user = User.query.filter_by(uuid=uuid).first()
                    if user:
                        return func(user, *args, **kwargs)
                    return abort(401)
                else:
                    return abort(401)
            except Exception as e:
                #TODO: catch jwt exceptions
                current_app.logger.debug(str(e))
                return abort(401)
        else:
            return abort(401)
    return wrapper
