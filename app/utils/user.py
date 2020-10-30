import time
import jwt
from random import randint
from flask import request
from flask import current_app as app


def generate_referrral_code(length=None, characters=None):
    if length is None:
        length = app.config['REFERRAL_CODE_LENGTH']
    
    if characters is None:
        characters = app.config['REFERRAL_CODE_CHARACTERS']

    result = ''
    for _ in range(0, length):
        result += characters[randint(0, len(characters) - 1)]

    return result


def generate_auth_token(payload):
    if 'exp' not in payload:
        payload.update({
            'exp': int(time.time()) + app.config['TOKEN_EXPIRATION']
        })
    
    token = jwt.encode(payload, key=app.config['SECRET_KEY'])

    return token.decode('utf-8')


def get_payload(token=None):
    if token is None:
        authorization = request.headers.get('Authorization')
        if not authorization.startswith('Bearer '):
            raise jwt.exceptions.DecodeError

        token = authorization.split(' ')[-1]
    payload = jwt.decode(token, key=app.config['SECRET_KEY'])

    return payload
