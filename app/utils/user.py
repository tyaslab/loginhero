from random import randint
from flask import current_app as app


def generate_referrral_code(length=None, characters=None):
    if length is None:
        length = app.config['REFERRAL_CODE_LENGTH']
    
    if characters is None:
        characters = app.config['REFERRAL_CODE_CHARACTERS']

    result = ''
    for i in range(0, length):
        result += characters[randint(0, len(characters))]

    return result
