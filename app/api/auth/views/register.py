import sqlalchemy as sa
from flask import request, g
from flask_babel import lazy_gettext as _
from app.utils.response import format_response
from app.api.auth.forms.registration_form import RegistrationForm
from app.models.auth import User, UserHasReferralCodes
from app.utils.connect_db import connect_db
from app.utils.user import generate_referrral_code
from app.utils.text import auto_trim
from werkzeug.security import generate_password_hash


def register():
    form = RegistrationForm()
    data = form.load(auto_trim(request.json or {}))

    connect_db()
    transaction = g.db.begin()
    referral_code = generate_referrral_code()
    password = generate_password_hash(data['password'])
    user_id = g.db.execute(
        User.insert().values(
            username=data['username'],
            password=password,
            name=data['name'],
            email=data['email'],
            referral_code=referral_code
        )
    ).lastrowid

    # save referral code
    # get user_id by referral code
    referral_code = data.get('referral_code')
    if referral_code:
        redeemed_user_id = g.db.execute(
            sa.select([User.c.id]).where(User.c.referral_code == data['referral_code'])
        ).scalar()

        g.db.execute(
            UserHasReferralCodes.insert().values(
                redeemed_referral_code=data['referral_code'],
                redeemed_user_id=redeemed_user_id,
                redeemer_user_id=user_id
            )
        )

    transaction.commit()

    result = {
        'id': user_id,
        'username': data['username'],
        'name': data['name'],
        'email': data['email'],
        'referral_code': referral_code
    }

    return format_response(data=result)
