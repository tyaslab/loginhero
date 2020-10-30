import json
import requests
from flask import request
from flask import current_app as app
from flask_babel import lazy_gettext as _
from app.utils.redis_adapter import connect_redis
from app.utils.response import format_response


def search_hero():
    '''
    Search hero from HERO_URL
    and return only first result
    '''
    q = request.args.get('q')
    if not q:
        return format_response(data=None, success=False, message=_('q param is required'), status_code=400)

    q = q.lower()
    redis = connect_redis()

    redis_key = f'hero:{q}'
    if redis.exists(redis_key):
        result = redis.get(redis_key)
    else:
        hero_data = get_hero_data()
        if hero_data is None:
            return format_response(data=None, success=False, message=_('No hero found'), status_code=404)
        
        hero_list = filter(lambda h: h[0].lower().startswith(q), hero_data)

        result = None
        for hero_item in hero_list:
            result = hero_item[1]
            break
        
        if result is None:
            return format_response(data=None, success=False, message=_('No hero found'), status_code=404)

        redis.set(redis_key, result)
    
    return format_response(data=result)


def get_hero_data():
    redis_key = 'hero-list'
    redis = connect_redis()
    if redis.exists(redis_key):
        result = redis.get(redis_key)
    else:
        hero_url = app.config['HERO_URL']
        try:
            response = requests.get(hero_url)
        except requests.exceptions.RequestException as e:
            app.logger.exception(e)

        if not response.ok:
            app.logger.error('Response from hero list is not ok')
            return None

        # NOTE: don't trust third party!
        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            app.logger.error(f'Cannot decode: {data}')
            return None

        result = list(data['data'].items())
        redis.set(redis_key, result)
    
    return result