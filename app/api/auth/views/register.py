from flask import request
from flask_babel import lazy_gettext as _
from app.utils.response import format_response
from app.api.auth.forms.registration_form import RegistrationForm
from app.models.auth import User
from app.utils.connect_db import connect_db
from app.utils.user import generate_referrral_code
from app.utils.text import auto_trim
from werkzeug.security import generate_password_hash


def register():
    form = RegistrationForm()
    data = form.load(auto_trim(request.json or {}))

    db = connect_db()
    referral_code = generate_referrral_code()
    password = generate_password_hash(data['password'])
    db.execute(
        User.insert().values(
            username=data['username'],
            password=password,
            name=data['name'],
            email=data['email'],
            referral_code=referral_code
        )
    )
    

    return format_response(data=None)
