def get_apidoc():
    apidoc = {
        'summary': 'Get User Detail',
        'description': 'Get User Detail',
        'tags': ['Auth'],
        'security': [
            {
                'bearerAuth': []
            }
        ],
        'parameters': [
            {
                'in': 'path',
                'name': 'username',
                'schema': {
                    'type': 'string'
                }
            }
        ],
        'responses': {
            '401': {
                'description': 'Unauthenticated user',
                'content': {
                    'application/json': {
                        'example': {
                            'code': '401',
                            'data': None,
                            'message': 'You are not authorized',
                            'meta': {},
                            'success': False
                        }
                    }
                }
            },
            '500': {
                'description': 'An error occured',
                'content': {
                    'application/json': {
                        'example': {
                            'code': 500,
                            'data': None,
                            'message': 'An error occured',
                            'meta': {},
                            'success': False
                        }
                    }
                }
            },
            '200': {
                'description': 'Success',
                'content': {
                    'application/json': {
                        'example': {
                            'code': 200,
                            'data': {
                                'email': 'adityadarmawan3@gmail.com',
                                'name': 'Abdul Abulbul Amir',
                                'registered_at': '2020-10-30 09:42:16',
                                'username': 'AdityaDarmawan4'
                            },
                            'message': 'Success',
                            'meta': {},
                            'success': True
                        }
                    }
                }
            }
        }
    }

    return apidoc
