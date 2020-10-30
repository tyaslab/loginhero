import pickle
from redis import Redis
from redis.exceptions import RedisError
from flask import current_app as app


class RedisAdapter:
    def __init__(self, redis_connection_params, prefix, app=None):
        self._redis_connection = Redis(**redis_connection_params)
        self.prefix = prefix
        self.init_app(app)

    def init_app(self, app):
        self.app = app

    def exists(self, key):
        key = f'{self.prefix}:{key}'

        try:
            result = self._redis_connection.exists(key)
        except RedisError as e:
            if self.app:
                self.app.logger.warning('Redis is down!')
                self.app.logger.exception(e)
            return False
        
        return result

    def get(self, key):
        key = f'{self.prefix}:{key}'

        try:        
            value = self._redis_connection.get(key)
        except RedisError as e:
            if self.app:
                self.app.logger.warning('Redis is down!')
                self.app.logger.exception(e)
            return None

        return pickle.loads(value)

    def set(self, key, value, timeout=None):
        key = f'{self.prefix}:{key}'

        if timeout is None:
            timeout = self.app.config.REDIS_TIMEOUT
        value = pickle.dumps(value)
        try:
            self._redis_connection.setex(key, timeout, value)
        except RedisError as e:
            if self.app:
                self.app.logger.warning('Redis is down!')
                self.app.logger.exception(e)
            return False

        return True

    def invalidate(self, key):
        key = f'{self.prefix}:{key}'

        try:
            keys = self._redis_connection.keys(key)
            for k in keys:
                self._redis_connection.delete(k)
        except RedisError as e:
            if self.app:
                self.app.logger.warning('Redis is down!')
                self.app.logger.exception(e)
            return False

        return True


def connect_redis():
    # initialize redis
    redis = RedisAdapter(
        dict(
            host=app.config.REDIS_HOST,
            port=app.config.get('REDIS_PORT', 6379),
            db=app.config.get('REDIS_DB', 0),
            password=app.config.get('REDIS_PASSWORD', None)
        ),
        prefix=app.config.REDIS_PREFIX,
        app=app
    )

    return redis
