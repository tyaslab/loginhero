import sqlalchemy as sa
import jwt
from flask import g
from app.utils.user import get_payload
from app.utils.response import format_response
from flask_babel import lazy_gettext as _
from app.models.auth import User
from app.utils.connect_db import connect_db
from app.utils.redis_adapter import connect_redis


def get_user_detail(username):
    try:
        get_payload()
    except jwt.exceptions.PyJWTError:
        # TODO: explain the error more obviously
        return format_response(data=None, success=False, message=_('You are not authorized'), status_code=401)

    # TODO: redis
    redis = connect_redis()
    redis_key = f'user-detail-{username}'
    if redis.exists(redis_key):
        result = redis.get(redis_key)
    else:
        connect_db()
        user = g.db.execute(
            sa.select([User]).where(User.c.username == username)
        ).fetchone()

        if not user:
            return format_response(data=None, success=False, message=_('User not found'), status_code=404)

        result = {
            'username': user.username,
            'name': user.name,
            'email': user.email,
            # 'referral_code': user.referral_code,
            'registered_at': user.created.strftime('%Y-%m-%d %H:%M:%S') if user.created is not None else None  # TODO: may other users see this?
        }

        redis.set(redis_key, result)

    return format_response(data=result)
