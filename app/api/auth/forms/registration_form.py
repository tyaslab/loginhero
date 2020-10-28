import sqlalchemy as sa
from flask_babel import lazy_gettext as _
from marshmallow import Schema, validates, validates_schema, ValidationError
from marshmallow.fields import String
from marshmallow.validate import Length
from app.utils.connect_db import connect_db
from app.models.auth import User


class RegistrationForm(Schema):
    username = String(required=True, allow_none=False,
        validate=[
            Length(min=1, error=_('Username is required'))
        ],
        error_messages={
            'required': _('Username is required'),
            'null': _('Username is required')
        }
    )
    password = String(required=True, allow_none=False,
        validate=[
            Length(min=1, error=_('Password is required'))
        ],
        error_messages={
            'required': _('Password is required'),
            'null': _('Password is required')
        }
    )
    confirm_password = String(required=True, allow_none=False,
        validate=[
            Length(min=1, error=_('Confirm Password is required'))
        ],
        error_messages={
            'required': _('Confirm Password is required'),
            'null': _('Confirm Password is required')
        }
    )
    name = String(required=True, allow_none=False,
        validate=[
            Length(min=1, error=_('Name is required'))
        ],
        error_messages={
            'required': _('Name is required'),
            'null': _('Name is required')
        }
    )
    email = String(required=True, allow_none=False,
        validate=[
            Length(min=1, error=_('Email is required'))
        ],
        error_messages={
            'required': _('Email is required'),
            'null': _('Email is required')
        }
    )
    referral_code = String(required=False, allow_none=True)

    @validates('username')
    def validate_username(self, username):
        db = connect_db()
        check = db.execute(
            sa.select([User.c.id]).where(User.c.username == username)
        ).scalar()

        if check:
            raise ValidationError(_('Username %(username)s already exists. Please input another username.'))

    @validates_schema(skip_on_field_errors=True)
    def validate_confirm_password(self, data, **kwargs):
        password = data['password']
        confirm_password = data['confirm_password']

        if confirm_password != password:
            raise ValidationError(_('Confirm password does not match'), 'confirm_password')
    
    @validates('email')
    def validate_email(self, email):
        db = connect_db()
        check = db.execute(
            sa.select([User.c.id]).where(User.c.email == email)
        ).scalar()

        if check:
            raise ValidationError(_('Email %(email)s already exists. Please input another email.'))

    @validates('referral_code')
    def validate_referral_code(self, referral_code):
        db = connect_db()
        check = db.execute(
            sa.select([User.c.id]).where(User.c.referral_code == referral_code)
        ).scalar()

        if not check:
            raise ValidationError(_('Invalid referral code'))
