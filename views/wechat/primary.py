import config
from flask import request
from views.wechat import api
from plugins.wechat.message_encrypt import WXBizMsgCrypt


@api.route('/signature/', methods=['GET'])
def signature():
    """验证消息的确来自微信服务器"""
    wechat_message_crypt = WXBizMsgCrypt.WXBizMsgCrypt(sToken=config.APP_SERVER_TOKEN,
                                                       sEncodingAESKey=config.APP_EncodingAESKey, sAppId=config.APP_ID)
    echostr = request.args.get('echostr', default="")
    return echostr
