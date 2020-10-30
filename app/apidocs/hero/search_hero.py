def get_apidoc():
    apidoc = {
        'summary': 'Search Hero',
        'description': 'Search Hero',
        'tags': ['Hero'],
        'security': [
            {
                'bearerAuth': []
            }
        ],
        'parameters': [
            {
                'in': 'query',
                'name': 'q'
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
                        'code': 200,
                        'data': {
                            'blurb': 'Unlike other foxes that roamed the woods of southern Ionia, Ahri had always felt a strange connection to the magical world around her; a connection that was somehow incomplete. Deep inside, she felt the skin she had been born into was an ill fit for ...',
                            'id': 'Ahri',
                            'image': {
                                'full': 'Ahri.png',
                                'group': 'champion',
                                'h': 48,
                                'sprite': 'champion0.png',
                                'w': 48,
                                'x': 48,
                                'y': 0
                            },
                            'info': {
                                'attack': 3,
                                'defense': 4,
                                'difficulty': 5,
                                'magic': 8
                            },
                            'key': '103',
                            'name': 'Ahri',
                            'partype': 'MP',
                            'stats': {
                                'armor': 20.88,
                                'armorperlevel': 3.5,
                                'attackdamage': 53.04,
                                'attackdamageperlevel': 3.0,
                                'attackrange': 550.0,
                                'attackspeedoffset': -0.065,
                                'attackspeedperlevel': 2.0,
                                'crit': 0.0,
                                'critperlevel': 0.0,
                                'hp': 514.4,
                                'hpperlevel': 80.0,
                                'hpregen': 6.505,
                                'hpregenperlevel': 0.6,
                                'movespeed': 330.0,
                                'mp': 334.0,
                                'mpperlevel': 50.0,
                                'mpregen': 6.0,
                                'mpregenperlevel': 0.8,
                                'spellblock': 30.0,
                                'spellblockperlevel': 0.0
                            },
                            'tags': [
                                'Mage',
                                'Assassin'
                            ],
                            'title': 'the Nine-Tailed Fox',
                            'version': '6.24.1'
                        },
                        'message': 'Success',
                        'meta': {},
                        'success': True
                    }
                }
            }
        }
    }

    return apidoc
