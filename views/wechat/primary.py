import json
import config
from flask import request
from init import wechat_api
from views.wechat import api
from plugins.wechat.message_encrypt import WXBizMsgCrypt


@api.route('/signature/', methods=['GET', 'POST'])
def signature():
    """验证消息的确来自微信服务器"""
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echo_str = request.args.get('echostr')
    wechat_message_crypt = WXBizMsgCrypt.WXBizMsgCrypt(sToken=config.APP_SERVER_TOKEN,
                                                       sEncodingAESKey=config.APP_EncodingAESKey, sAppId=config.APP_ID)

    if request.method == "POST":
        print(
            wechat_message_crypt.DecryptMsg(request.data, sMsgSignature=signature, sTimeStamp=timestamp, sNonce=nonce))
    return wechat_message_crypt.verity_token(signature=signature, timestamp=timestamp, nonce=nonce,
                                             echo_str=echo_str)


@api.route('/menu/create/')
def create_menu():
    """创建菜单"""
    with open("wechat_menu_config.json", "r", encoding="utf-8") as file:
        # menu_config = json.load(file)
        # print(file.read())
        wechat_api.create_menu(body=file.read().encode(encoding='utf-8'), port="8090")
