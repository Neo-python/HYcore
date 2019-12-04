from flask import request
from init import wechat_api, wechat_message_crypt
from views.wechat import api


@api.route('/signature/', methods=['GET', 'POST'])
def signature():
    """验证消息的确来自微信服务器"""
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echo_str = request.args.get('echostr')

    if request.method == "POST":
        error_code, xml = wechat_message_crypt.DecryptMsg(sPostData=request.get_data().decode(),
                                                          sMsgSignature=signature,
                                                          sTimeStamp=timestamp, sNonce=nonce)
        print(error_code, xml, request.get_data().decode())
        print(signature, timestamp, nonce)
        return 'ok'
    return wechat_message_crypt.verity_token(signature=signature, timestamp=timestamp, nonce=nonce,
                                             echo_str=echo_str)


@api.route('/menu/create/')
def create_menu():
    """创建菜单"""
    with open("wechat_menu_config.json", "r", encoding="utf-8") as file:
        # menu_config = json.load(file)
        # print(file.read())
        wechat_api.create_menu(body=file.read().encode(encoding='utf-8'), port="8090")
