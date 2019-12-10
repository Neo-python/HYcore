import sys
import config
import logging
import redis
from flask import Flask
from celery import Celery
from pymysql import install_as_MySQLdb
from plugins.HYplugins.sms import SMS
from plugins.HYplugins.orm import db
from plugins import wechat
from plugins.wechat.wechat_encrypt.WXBizMsgCrypt import WXBizMsgCrypt
from plugins.HYplugins.common.position import Position
from sts.sts import Sts
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

# celery
celery = Celery(__name__, broker=config.CELERY_BROKER_URL, backend=config.CELERY_BACKEND_URL,
                include=['asynchronous.periodic_task'])

# 短信
sms = SMS(app_id=config.SMS_APP_ID, app_key=config.SMS_APP_KEY)
# 应用
install_as_MySQLdb()
# cos
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
cos_config = CosConfig(Region=config.region, SecretId=config.SecretId, SecretKey=config.SecretKey, Token=config.token,
                       Scheme=config.scheme)
client = CosS3Client(cos_config)
# cos token
cos_sts = Sts(config.sts_config)

# redis
pool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB, decode_responses=True)
Redis = redis.StrictRedis(connection_pool=pool)
# 微信
wechat_message_crypt = WXBizMsgCrypt(sToken=config.APP_SERVER_TOKEN,
                                     sEncodingAESKey=config.APP_EncodingAESKey, sAppId=config.APP_ID)
wechat_api = wechat.WechatApi(app_id=config.APP_ID, app_secret=config.APP_SECRET, redis=Redis)
position = Position(key=config.POSITION_APP_KEY)
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def register_blueprint(app):
    """注册蓝图"""
    from views.common import api
    app.register_blueprint(api)
    from views.wechat import api
    app.register_blueprint(api)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    # app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)
    return app


class CoreApi:
    pass


core_api = CoreApi()
