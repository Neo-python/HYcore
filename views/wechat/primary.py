from flask import request
from views.wechat import api, wechat_message_crypt


@api.route('/signature/', methods=['GET'])
def signature():
    """验证消息的确来自微信服务器"""
    echostr = request.args.get('echostr')
    return echostr
