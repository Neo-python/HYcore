"""微信服务号相关接口"""
import config
from flask import Blueprint
from plugins.wechat.message_encrypt import WXBizMsgCrypt

api = Blueprint('wechat', __name__, url_prefix='/wechat')

from views.common.primary import *

wechat_message_crypt = WXBizMsgCrypt.WXBizMsgCrypt(sToken=config.APP_SERVER_TOKEN,
                                                   sEncodingAESKey=config.APP_EncodingAESKey, sAppId=config.APP_ID)
