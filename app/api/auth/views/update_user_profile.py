import sqlalchemy as sa
import jwt
from flask import request, g
from app.utils.user import get_payload
from app.utils.response import format_response
from flask_babel import lazy_gettext as _
from app.models.auth import User
from app.utils.connect_db import connect_db
from app.api.auth.forms.profile_form import ProfileForm
from werkzeug.security import generate_password_hash


def update_user_profile():
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

    form = ProfileForm(context={'user': user}, partial=True)
    data = form.load(request.json or {})

    values_to_update = {
        'modified': sa.func.NOW()
    }
    for key in data:
        if key in ['username', 'name', 'email']:
            values_to_update.update({
                key: data[key]
            })
        elif key == 'password':
            values_to_update.update({
                'password': generate_password_hash(data[key])
            })

    transaction = g.db.begin()
    g.db.execute(
        User.update().values(**values_to_update).where(User.c.id == user_id)
    )
    transaction.commit()

    return format_response(data=None)
