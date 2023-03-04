from flask import Blueprint, request
from flask_login import login_required

from app.index import index
from app.diary import diary
from auth.login import login, logout, user
from web.response import build_response


routes = Blueprint('routes', __name__)


@routes.route('/')
def route_index():
    return build_response(index)


@routes.route('/diary/<month>')
def route_diary(month: str):
    return build_response(diary, month=month)


@routes.route('/login')
def route_login():
    user_id = request.args.get('user_id')
    password = request.args.get('password')

    return build_response(login, user_id=user_id, password=password)


@routes.route('/user')
@login_required
def route_user():
    return build_response(user)


@routes.route('/logout')
def route_logout():
    return build_response(logout)
