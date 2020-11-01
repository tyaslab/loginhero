import sqlalchemy as sa
import jwt
from flask import request, g
from flask_babel import lazy_gettext as _
from app.utils.user import get_payload
from app.utils.response import format_response
from app.utils.connect_db import connect_db
from app.models.auth import User
from app.utils.redis_adapter import connect_redis


def get_user_list():
    # TODO: pagination
    try:
        get_payload()
    except jwt.exceptions.PyJWTError:
        # TODO: explain the error more obviously
        return format_response(data=None, success=False, message=_('You are not authorized'), status_code=401)
    
    redis = connect_redis()
    q = ''
    if request.method == 'POST':
        try:
            params = request.json or {}
            q = params.get('q', '')
        except:
            # TODO: except more correctly
            q = ''
    redis_key = f'user-list:q-{q}'
    if redis.exists(redis_key):
        result = redis.get(redis_key)
    else:
        connect_db()
        sql = sa.select([User]).order_by(sa.desc(User.c.created))
        if q:
            sql = sql.where(
                sa.or_(
                    User.c.name.like(f'%%{q}%%'),
                    User.c.username.like(f'%%{q}%%')
                )
                
            )
        
        user_list = g.db.execute(sql).fetchall()

        result = []
        for user in user_list:
            result.append({
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'registered_at': user.created.strftime('%Y-%m-%d %H:M:S') if user.created is None else None
            })
        
        redis.set(redis_key, result)
    
    return format_response(data=result)
