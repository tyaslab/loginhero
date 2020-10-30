import sqlalchemy as sa
from flask import Flask, g, request
from flask_babel import Babel
from flask_babel import lazy_gettext as _
from app import config
from marshmallow import ValidationError
from app.utils.response import format_response


app = Flask(__name__)
app.config.from_object(config)

# initialize babel
babel = Babel(app=app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'id'])


@app.after_request
def disconnect_db(response):
    if hasattr(g, 'db'):
        g.db.close()
    
    return response


@app.errorhandler(ValidationError)
def handle_validation_error(exception):
    # TODO: I don't like list of messages per field so I put only first error message per field
    messages = exception.messages
    data = {}
    for k in messages:
        if isinstance(messages[k], list):
            data.update({k: messages[k][0]})
        else:
            data.update({k: messages[k]})
    return format_response(data=data, success=False, status_code=400, message=_('Please check your data'))


from app.api import blueprint as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
