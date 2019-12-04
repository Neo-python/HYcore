"""微信服务号相关接口"""
from flask import Blueprint

api = Blueprint('wechat', __name__, url_prefix='/wechat')

from views.wechat.primary import *
from models.business import *
from models.common import *
from models.system import *
from models.user import *