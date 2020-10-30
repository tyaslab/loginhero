import sqlalchemy as sa
from flask import g
from flask_babel import lazy_gettext as _
from marshmallow import Schema, validates, ValidationError
from marshmallow.fields import String
from marshmallow.validate import Length
from app.utils.connect_db import connect_db
from app.models.auth import User, UserHasReferralCodes


class InputReferralCodeForm(Schema):
    referral_code = String(required=True, allow_none=False,
        error_messages={
            'required': _('Referral code is required'),
            'null': _('Referal code is required')
        },
        validate=[
            Length(min=1, error=_('Referral code is required'))
        ]
    )

    @validates('referral_code')
    def validate_referral_code(self, referral_code):
        # check if user has redeemed referral code before
        user_id = self.context.get('user_id')
        uhrc = UserHasReferralCodes.alias('uhrc')
        connect_db()
        user_has_redeemed = g.db.execute(
            sa.select([uhrc.c.id]).where(uhrc.c.redeemer_user_id == user_id)
        ).fetchone()

        if user_has_redeemed:
            raise ValidationError(_('You already redeemed referral code'))

        # check the owner of referral code
        user_referral_code = g.db.execute(
            sa.select([User.c.id]).where(User.c.referral_code == referral_code)
        ).scalar()

        if not user_referral_code:
            raise ValidationError(_('Invalid referral code'))

        if user_id == user_referral_code:
            raise ValidationError(_('You cannot redeem your own referral code'))

        self.context['user_referral_code'] = user_referral_code
