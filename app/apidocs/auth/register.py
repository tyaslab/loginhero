def get_apidoc():
    apidoc = {
        'summary': 'Register',
        'description': 'Register',
        'tags': ['Auth'],
        'security': [],
        'requestBody': {
            'description': 'JSON Object containing registration information',
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
                            },
                            'referral_code': {
                                'type': 'string',
                                'required': False
                            }
                        }
                    },
                    'example': {
                        'username': 'AdityaDarmawan2',
                        'password': 'adityadarmawan2',
                        'email': 'adityadarmawan2@gmail.com',
                        'name': 'Aditya Darmawan2',
                        'confirm_password': 'adityadarmawan2'
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
                            'confirm_password': 'Confirm Password is required',
                            'email': 'Email is required',
                            'name': 'Name is required',
                            'password': 'Password is required'
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
                                'email': 'adityadarmawan2@gmail.com',
                                'id': 0,
                                'name': 'Aditya Darmawan2',
                                'referral_code': None,
                                'username': 'AdityaDarmawan2'
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
