import sqlalchemy as sa
from flask import request
from app.api.auth.forms.login_form import LoginForm
from app.utils.response import format_response
from app.utils.user import generate_auth_token


def login():
    form = LoginForm()
    form.load(request.json or {})
    user = form.context.get('user')

    result = {
        'id': user.id,
        'name': user.name,
        'username': user.username,
        'email': user.email
    }

    auth_token = generate_auth_token(result)
    result.update({
        'auth_token': auth_token
    })

    # NOTE: do we need exp ?
    del result['exp']

    return format_response(data=result)
