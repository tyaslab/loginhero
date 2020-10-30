import sqlalchemy as sa
from flask import g
from flask_babel import lazy_gettext as _
from marshmallow import Schema, validates, validates_schema, ValidationError, EXCLUDE
from marshmallow.fields import String
from marshmallow.validate import Length, Regexp
from app.utils.connect_db import connect_db
from app.models.auth import User
from werkzeug.security import check_password_hash


class LoginForm(Schema):
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
    password = String(required=True, allow_none=False,
        validate=[
            Length(min=1, error=_('Password is required'))
        ],
        error_messages={
            'required': _('Password is required'),
            'null': _('Password is required')
        }
    )

    class Meta:
        unknown = EXCLUDE

    @validates_schema(skip_on_field_errors=True)
    def validate_username(self, data, **kwargs):
        connect_db()
        user = g.db.execute(
            sa.select([User]).where(User.c.username == data['username'])
        ).fetchone()

        if not user:
            raise ValidationError(_('Invalid username'), 'username')

        
        if not check_password_hash(user.password, data['password']):
            raise ValidationError(_('Invalid password'), 'password')

        self.context['user'] = user
