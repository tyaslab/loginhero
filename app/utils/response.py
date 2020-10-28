from flask import jsonify
from flask_babel import lazy_gettext as _


def format_response(data, meta={}, success=True, message=None, status_code=200, code=None):
    if message is None:
        message = _('Success')
    
    if code is None:
        status_code = code

    return jsonify({
        data=data,
        meta=meta,
        success=success,
        message=message
    }), status_code
