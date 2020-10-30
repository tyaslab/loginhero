from importlib import import_module
from flask import jsonify
import json


def import_apidoc(apidoc_string):
    # TODO: relative import
    apidoc = import_module('app.apidocs.%s' % apidoc_string)

    return apidoc.get_apidoc()


def generate_apidocs():
    apidocs = {
        'openapi': '3.0.0',
        'info': {
            'version': '1.0',
            'title': 'Login Hero',
            'license': {
                'name': 'ALL RIGHTS ARE NOT RESERVED'
            }
        },
        'servers': [
            {
                'url': '/api/v1',
                'description': 'Local'
            }
        ],
        'paths': {
            '/auth/register': {
                'post': import_apidoc('auth.register')
            },
            '/auth/login': {
                'post': import_apidoc('auth.login')
            },
            '/auth/input-referral-code': {
                'post': import_apidoc('auth.input_referral_code')
            },
            '/auth/user/list': {
                'get': import_apidoc('auth.get_user_list')
            },
            '/auth/user/detail/:username': {
                'get': import_apidoc('auth.get_user_detail')
            },
            '/auth/user/profile': {
                'get': import_apidoc('auth.get_user_profile'),
                'put': import_apidoc('auth.update_user_profile'),
            },
            '/hero/search': {
                'get': import_apidoc('hero.search_hero'),
            },
        },
        'components': {
            'securitySchemes': {
                'bearerAuth': {
                    'type': 'http',
                    'scheme': 'bearer',
                    'bearerFormat': 'jwt',
                    'description': 'API Authorization'
                }
            }
        }
    }

    return jsonify(apidocs)
