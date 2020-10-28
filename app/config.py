DEBUG = False
ENV = 'production'
PORT = 5000

REDIS_PREFIX = 'loginhero'


try:
    from app.local_config import *
except ImportError:
    pass
