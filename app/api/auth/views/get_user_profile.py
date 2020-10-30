import sqlalchemy as sa
import jwt
from flask import g
from app.utils.user import get_payload
from app.utils.response import format_response
from flask_babel import lazy_gettext as _
from app.models.auth import User
from app.utils.connect_db import connect_db


def get_user_profile():
    try:
        payload = get_payload()
    except jwt.exceptions.PyJWTError:
        # TODO: explain the error more obviously
        return format_response(data=None, success=False, message=_('You are not authorized'), status_code=401)

    user_id = payload['id']
    connect_db()
    user = g.db.execute(
        sa.select([User]).where(User.c.id == user_id)
    ).fetchone()

    result = {
        'username': user.username,
        'name': user.name,
        'email': user.email,
        'referral_code': user.referral_code,
        'registered_at': user.created.strftime('%Y-%m-%d %H:%M:%S') if user.created is not None else None
    }

    return format_response(data=result)
