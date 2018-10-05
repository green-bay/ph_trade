import pytest
from app.db import db
from app.models.users import User
from app.models.classifieds import ClassifiedAd, ClassifiedTags

# helpers
def create_user():
    return User.create(email="test@test.pl",password="test")

def get_default_ads_vals():
    return {
        'name': 'TestAd',
        'publisher': 'zzz',
        'user_id': None        
    }

def create_ad(vals):
    return ClassifiedAd.create(**vals)

def create_ad_tag(name):
    return ClassifiedTags.create(name=name)
# end helpers

def test_config(app):
    assert app.config['TESTING'] == True

def test_encode_auth_token(app):
    with app.app_context():
        user = create_user()
        auth_token = user.encode_auth_token(user.id)
        assert isinstance(auth_token, bytes)

def test_decode_auth_token(app):
    with app.app_context():
        user = create_user()
        auth_token = user.encode_auth_token(user.uuid)
        assert isinstance(auth_token, bytes)
        assert User.decode_auth_token(auth_token) == str(user.uuid)

def test_create_add(app):
    with app.app_context():
        user = create_user()
        ad_vals = get_default_ads_vals()
        ad_vals['user_id'] = user.id
        ad = create_ad(ad_vals)
        assert ad.user_id == user.id

def test_ad_tags(app):
    with app.app_context():
        user = create_user()
        ad_vals = get_default_ads_vals()
        ad_vals['user_id'] = user.id
        tag1 = create_ad_tag('wiecha')
        tag2 = create_ad_tag('susz')
        ad_vals['categories'] = [tag1, tag2]
        ad = create_ad(ad_vals)
        assert len(ad.categories) == 2
