DEBUG = False
ENV = 'production'
PORT = 5000

REDIS_PREFIX = 'loginhero'

REFERRAL_CODE_LENGTH = 10
REFERRAL_CODE_CHARACTERS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

TOKEN_EXPIRATION = 3 * 60 * 60  # in seconds

REDIS_HOST = 'localhost'
REDIS_PREFIX = 'loginhero'
REDIS_TIMEOUT = 5 * 60  # in seconds

HERO_URL = 'https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json'

try:
    from app.local_config import *
except ImportError:
    pass
