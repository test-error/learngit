#coding: utf8
from flask import Blueprint
import flask

bp = Blueprint('cms',__name__,subdomain='cms')

@bp.route('/')
def index():
    return u'这是cms首页'