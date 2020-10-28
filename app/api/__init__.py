from flask import Blueprint
from app.api.auth.views.register import register
from app.api.auth.views.login import login
from app.api.auth.views.get_user_list import get_user_list
from app.api.auth.views.get_user_detail import get_user_detail
from app.api.auth.views.get_user_profile import get_user_profile
from app.api.auth.views.update_user_profile import update_user_profile

from app.api.hero.views.search_hero import search_hero

blueprint = Blueprint('api', __name__)
blueprint.add_url_rule('/auth/register', endpoint='auth_register', view_func=register)
blueprint.add_url_rule('/auth/login', endpoint='auth_login', view_func=login)
blueprint.add_url_rule('/auth/user/list', endpoint='auth_user_list', view_func=get_user_list)
blueprint.add_url_rule('/auth/user/detail/<int:id>', endpoint='auth_user_detail', view_func=get_user_detail)
blueprint.add_url_rule('/auth/user/profile', endpoint='auth_user_profile', view_func=get_user_profile)

blueprint.add_url_rule('/hero/search', endpoint='hero_search_hero', view_func=search_hero)
