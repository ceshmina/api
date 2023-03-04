from flask import Blueprint

from app.index import index
from app.diary import diary


routes = Blueprint('routes', __name__)


@routes.route('/')
def route_index():
    return index()


@routes.route('/diary')
def route_diary():
    return diary()
