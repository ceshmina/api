from flask import Blueprint

from app.index import index
from app.diary import diary
from web.response import build_response


routes = Blueprint('routes', __name__)


@routes.route('/')
def route_index():
    return build_response(index)


@routes.route('/diary/<month>')
def route_diary(month: str):
    return build_response(diary, month=month)
