from functools import wraps
from flask import request, current_app
from flask_restplus import abort
from app.models.users import User
from flask_login import current_user


def require_auth(func):
    """Secure method decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return func(*args, **kwargs)
        return abort(401)
    return wrapper
