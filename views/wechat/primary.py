import xmltodict
from flask import request
from init import wechat_api, wechat_message_crypt
from views.wechat import api
from plugins.wechat.primary import Event


@api.route('/', methods=['GET'])
def signature():
    """验证消息的确来自微信服务器"""
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echo_str = request.args.get('echostr')

    return wechat_message_crypt.verity_token(signature=signature, timestamp=timestamp, nonce=nonce,
                                             echo_str=echo_str)


@api.route('/', methods=['POST'])
def event():
    """公众号事件"""
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    msg_signature = request.args.get('msg_signature')
    _, xml = wechat_message_crypt.DecryptMsg(sPostData=request.get_data().decode(),
                                             sMsgSignature=msg_signature, sTimeStamp=timestamp, sNonce=nonce)
    content = xmltodict.parse(xml_input=xml)['xml']

    event_export = Event(data=content, wechat_message_crypt=wechat_message_crypt)
    return event_export.handle()


@api.route('/menu/create/')
def create_menu():
    """创建菜单"""
    with open("wechat_menu_config.json", "r", encoding="utf-8") as file:
        # menu_config = json.load(file)
        # print(file.read())
        wechat_api.create_menu(body=file.read().encode(encoding='utf-8'), port="8090")
