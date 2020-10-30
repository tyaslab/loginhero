def get_apidoc():
    apidoc = {
        'summary': 'Input referral code',
        'description': 'Input referral code',
        'tags': ['Auth'],
        'security': [
            {
                'bearerAuth': []
            }
        ],
        'requestBody': {
            'description': 'JSON Object containing referral code information',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'referral_code': {
                                'type': 'string',
                                'required': True
                            }
                        }
                    },
                    'example': {
                        'referral_code': 'ASDFGHJKL'
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
                            'referral_code': 'Invalid referral code'
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
                            'message': 'Successfully redeemed referal code',
                            'meta': {},
                            'success': True
                        }
                    }
                }
            }
        }
    }

    return apidoc
