def get_apidoc():
    apidoc = {
        'summary': 'Login',
        'description': 'Login',
        'tags': ['Auth'],
        'security': [],
        'requestBody': {
            'description': 'JSON Object containing login information',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'username': {
                                'type': 'string',
                                'required': True
                            },
                            'password': {
                                'type': 'string',
                                'required': True
                            }
                        }
                    },
                    'example': {
                        'username': 'AdityaDarmawan',
                        'password': 'wow'
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
                            'password': 'Invalid password'
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
                            'data': {
                                'auth_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwibmFtZSI6IkFkaXR5YSBEYXJtYXdhbiIsInVzZXJuYW1lIjoiQWRpdHlhRGFybWF3YW4iLCJlbWFpbCI6ImFkaXR5YWRhcm1hd2FuM0BnbWFpbC5jb20iLCJleHAiOjE2MDQwNjMzMTZ9.TQ3hYfO0YWERowvm3PfhJcYopyJB0LC8QZVbgrikb3c',
                                'email': 'adityadarmawan3@gmail.com',
                                'id': 1,
                                'name': 'Aditya Darmawan',
                                'username': 'AdityaDarmawan'
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
