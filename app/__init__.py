import sqlalchemy as sa
from flask import Flask, g, request
from flask_babel import Babel
from flask_babel import lazy_gettext as _
from app import config
from marshmallow import ValidationError
from flask import jsonify
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


if app.config.get('ENABLE_APIDOCS', True):
    from app.apidocs import generate_apidocs
    from flask import render_template

    def get_apidocs_config():
        # TODO: apidocs configs goes here
        return jsonify({})

    def show_apidocs():
        return render_template('apidocs.html', STATIC_URL='/static/')

    app.add_url_rule('/api/v1/apidocs-config', endpoint='get_apidocs_config', view_func=get_apidocs_config)
    app.add_url_rule('/api/v1/apidocs.json', endpoint='generate_apidocs', view_func=generate_apidocs)
    app.add_url_rule('/api/v1/apidocs', endpoint='apidocs', view_func=show_apidocs)
