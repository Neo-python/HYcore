"""微信相关接口"""
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
        result = requests.post(url=url, json=body)
        print(result)
        print(result.json())
