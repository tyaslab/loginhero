import sqlalchemy as sa
from flask import Flask, g, request
from flask_babel import Babel
from app import config


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


from app.api import blueprint as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
