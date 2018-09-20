"""
REST API resource routing
part of flask-restplus
"""

from datetime import datetime
from flask import request
from flask_restplus import Resource

from .security import require_auth
from . import api_rest


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
