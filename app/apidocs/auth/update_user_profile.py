def get_apidoc():
    apidoc = {
        'summary': 'Update User Profile',
        'description': 'Update User Profile',
        'tags': ['Auth'],
        'security': [
            {
                'bearerAuth': []
            }
        ],
        'requestBody': {
            'description': 'JSON Object containing profile information',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'email': {
                                'type': 'string',
                                'required': True
                            },
                            'username': {
                                'type': 'string',
                                'required': True
                            },
                            'password': {
                                'type': 'string',
                                'required': True
                            },
                            'confirm_password': {
                                'type': 'string',
                                'required': True
                            },
                            'name': {
                                'type': 'string',
                                'required': True
                            }
                        }
                    },
                    'example': {
                        'email': 'adityadarmawan3@gmail.com',
                        'password': 'wow',
                        'confirm_password': 'wow',
                        'name': 'Abdul Abulbul Amir',
                        'username': 'AdityaDarmawan4'
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
            '400': {
                'description': 'Bad request',
                'content': {
                    'application/json': {
                        'code': 400,
                        'data': {
                            'username': 'Username AdityaDarmawan2 already exists. Please input another username.'
                        },
                        'message': 'Please check your data',
                        'meta': {},
                        'success': False
                    }
                }
            },
            '200': {
                'description': 'Success',
                'content': {
                    'application/json': {
                        'example': {
                            'code': 200,
                            'data': None,
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
