def get_apidoc():
    apidoc = {
        'summary': 'Get User List',
        'description': 'Get User List',
        'tags': ['Auth'],
        'security': [
            {
                'bearerAuth': []
            }
        ],
        'requestBody': {
            'description': 'JSON Object containing search query information',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'q': {
                                'type': 'string',
                                'required': True
                            }
                        }
                    },
                    'example': {
                        'q': 'siny'
                    }
                }
            }
        },
        'parameters': [],
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
                            'data': [
                                {
                                    'id': 1,
                                    'name': 'Aditya Darmawan1',
                                    'registered_at': None,
                                    'username': 'AdityaDarmawan1'
                                },
                                {
                                    'id': 2,
                                    'name': 'Aditya Darmawan2',
                                    'registered_at': None,
                                    'username': 'AdityaDarmawan2'
                                }
                            ],
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
