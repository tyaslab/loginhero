import sqlalchemy as sa
from flask import g
from flask import current_app as app


def connect_db():
    if not hasattr(g, 'db'):
        # create db engine
        db = sa.create_engine(app.config['DB'])
        g.db = db.connect()
