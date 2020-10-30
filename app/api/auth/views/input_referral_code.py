import sqlalchemy as sa
import jwt
from marshmallow import ValidationError
from flask import request, g
from flask_babel import lazy_gettext as _
from app.utils.connect_db import connect_db
from app.utils.user import get_payload
from app.utils.response import format_response
from app.models.auth import User, UserHasReferralCodes
from app.api.auth.forms.input_referral_code_form import InputReferralCodeForm


def input_referral_code():
    try:
        payload = get_payload()
    except jwt.exceptions.PyJWTError:
        # TODO: explain the error more obviously
        return format_response(data=None, success=False, message=_('You are not authorized'), status_code=401)

    form = InputReferralCodeForm(context={'user_id': payload['id']})
    data = form.load(request.json or {})
    user_referral_code = form.context.get('user_referral_code')

    transaction = g.db.begin()
    g.db.execute(
        UserHasReferralCodes.insert().values(
            redeemed_referral_code=data['referral_code'],
            redeemed_user_id=user_referral_code,
            redeemer_user_id=payload['id']
        )
    )
    transaction.commit()

    return format_response(
        data=None,
        message=_('Successfully redeemed referal code')
    )
