#! /usr/bin/env python3

from app import app
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        if args[1] == 'create-table':
            from app.models import meta_db
            from app.utils.connect_db import connect_db
            from flask import g
            with app.app_context():
                connect_db()
                meta_db.create_all(g.db)
    else:
        app.run()
