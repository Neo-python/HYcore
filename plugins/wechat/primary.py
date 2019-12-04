"""微信相关接口"""
import time
import config
import requests


class WechatApi:
    """微信接口"""

    access_token_redis_key = "WechatAccessToken"

    def __init__(self, app_id: str, app_secret: str):
        """对象初始化"""
        self.app_id = app_id
        self.app_secret = app_secret

    def get_open_id(self, code: str, port: str) -> str:
        """获取open_id
        :param code: 微信码
        :param port: 应用端口号
        :return:
        """
        account = self.get_account(port=port)
        url = f'https://api.weixin.qq.com/sns/jscode2session?appid={account["app_id"]}&secret={account["secret"]}&js_code={code}&grant_type=authorization_code'
        result = requests.get(url)
        result = result.json()
        return result['openid']

    def get_account(self, port: str) -> dict:
        """获取小程序账号信息,AppID/AppSecret
        :param port: 应用端口号
        :return:
        """
        return config.WECHAT_ACCOUNTS[port]

    def get_access_token(self, port: str) -> str:
        """优先从redis缓存中获取
        :param port: 应用端口号
        :return:
        """
        from init import Redis
        access_token = Redis.get(self.access_token_redis_key + port)
        if access_token:
            return access_token
        else:
            return self.update_access_token(port=port)

    def update_access_token(self, port: str) -> str:
        """向腾讯服务器请求
        :param port: 应用端口号
        :return:
        """
        from init import Redis
        account = self.get_account(port=port)
        url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={account["app_id"]}&secret={account["secret"]}'

        result = requests.get(url=url)
        result = result.json()
        access_token = result['access_token']
        Redis.set(self.access_token_redis_key + port, access_token, ex=7140)
        return access_token

    def create_menu(self, body: dict, port: str):
        """创建微信菜单
        :param body: 菜单数据
        :param port: 应用端口号
        :return:
        """
        access_token = self.get_access_token(port=port)

        print(access_token)
        url = f'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={access_token}'
        result = requests.post(url=url, data=body)
        print(result.json())


class Event(object):
    """处理各类事件"""

    def __init__(self, data: dict, nonce: str, wechat_message_crypt):
        self.data = data
        self.wechat_message_crypt = wechat_message_crypt
        self.reply_message = None
        self.nonce = nonce

    def event(self):
        """事件类型事件"""
        event = self.data['Event']

        if event == 'subscribe':
            self.event_subscribe()
        elif event == 'unsubscribe':
            self.event_unsubscribe()
        elif event == 'view_miniprogram':
            pass

    def event_subscribe(self):
        """关注和类型事件"""

    def event_unsubscribe(self):
        """取消关注类型事件"""

    def text(self):
        """文本类型事件"""
        result = self.reply_text(to_user=self.data['FromUserName'], from_user=self.data['ToUserName'],
                                 content=self.data['Content'])
        self.reply_message = result

    def handle(self):
        """启动逻辑的入口"""
        msg_type = self.data['MsgType']

        if msg_type == 'event':
            self.event()
        if msg_type == 'text':
            self.text()
        if self.reply_message:
            return self.reply_message
        else:
            return 'success'

    def reply_text(self, to_user: str, from_user: str, content: str):
        """回复文本消息"""
        create_time = str(int(time.time()))
        text = f"""<xml><ToUserName><![CDATA[{to_user}]]></ToUserName><FromUserName><![CDATA[{from_user}]]></FromUserName><CreateTime>12345678</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[{content}]]></Content></xml>"""
        rep, xml = self.wechat_message_crypt.EncryptMsg(text, self.nonce)
        if rep == 0:
            return xml
        else:
            return None
