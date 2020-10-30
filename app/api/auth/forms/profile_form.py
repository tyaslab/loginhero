import sqlalchemy as sa
from flask import g
from flask_babel import lazy_gettext as _
from marshmallow import Schema, validates, validates_schema, ValidationError, EXCLUDE
from marshmallow.fields import String
from marshmallow.validate import Length, Regexp, Email
from app.utils.connect_db import connect_db
from app.models.auth import User


class ProfileForm(Schema):
    username = String(required=True, allow_none=False,
        validate=[
            Length(min=1, error=_('Username is required')),
            Regexp(r'^[a-zA-Z_\-0-9]+$', error=_('Username cannot contain space and can only contain a-z,_,0-9'))
        ],
        error_messages={
            'required': _('Username is required'),
            'null': _('Username is required')
        }
    )
    password = String(required=False, allow_none=True,
        validate=[
            Length(min=1, error=_('Password is required'))
        ],
        error_messages={
            'required': _('Password is required'),
            'null': _('Password is required')
        }
    )
    confirm_password = String(required=False, allow_none=True,
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
            Length(min=1, error=_('Email is required')),
            Email(error=_('Invalid email format'))
        ],
        error_messages={
            'required': _('Email is required'),
            'null': _('Email is required')
        }
    )

    class Meta:
        unknown = EXCLUDE

    @validates('username')
    def validate_username(self, username):
        user = self.context.get('user')
        connect_db()
        check = g.db.execute(
            sa.select([User.c.id]).where(
                sa.and_(
                    User.c.username == username,
                    User.c.id != user.id
                )
            )
        ).scalar()

        if check:
            raise ValidationError(_('Username %(username)s already exists. Please input another username.', username=username))

    @validates_schema(skip_on_field_errors=True)
    def validate_confirm_password(self, data, **kwargs):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and not confirm_password:
            raise ValidationError(_('Confirm password is required'), 'confirm_password')

        if password and confirm_password and confirm_password != password:
            raise ValidationError(_('Confirm password does not match'), 'confirm_password')
    
    @validates('email')
    def validate_email(self, email):
        user = self.context.get('user')
        connect_db()
        check = g.db.execute(
            sa.select([User.c.id]).where(
                sa.and_(
                    User.c.email == email,
                    User.c.id != user.id
                )
            )
        ).scalar()

        if check:
            raise ValidationError(_('Email %(email)s already exists. Please input another email.', email=email))
