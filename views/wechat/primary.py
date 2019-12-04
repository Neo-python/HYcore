import json
import config
from flask import request
from init import wechat_api
from views.wechat import api
from plugins.wechat.message_encrypt import WXBizMsgCrypt


@api.route('/signature/', methods=['GET'])
def signature():
    """验证消息的确来自微信服务器"""
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echo_str = request.args.get('echostr')
    wechat_message_crypt = WXBizMsgCrypt.WXBizMsgCrypt(sToken=config.APP_SERVER_TOKEN,
                                                       sEncodingAESKey=config.APP_EncodingAESKey, sAppId=config.APP_ID)
    return wechat_message_crypt.verity_token_get(signature=signature, timestamp=timestamp, nonce=nonce,
                                                 echo_str=echo_str)


@api.route('/menu/create/')
def create_menu():
    """创建菜单"""
    with open("wechat_menu_config.json", "r", encoding="utf-8") as file:
        menu_config = json.load(file)
        wechat_api.create_menu(body=menu_config, port="8090")
