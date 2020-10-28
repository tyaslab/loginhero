DEBUG = False
ENV = 'production'
PORT = 5000

REDIS_PREFIX = 'loginhero'

REFERRAL_CODE_LENGTH = 10
REFERRAL_CODE_CHARACTERS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


try:
    from app.local_config import *
except ImportError:
    pass
