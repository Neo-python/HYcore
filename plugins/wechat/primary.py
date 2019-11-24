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
        """获取open_id"""
        account = self.get_account(port=port)
        url = f'https://api.weixin.qq.com/sns/jscode2session?appid={account["app_id"]}&secret={account["secret"]}&js_code={code}&grant_type=authorization_code'
        result = requests.get(url)
        result = result.json()
        print(result)
        return result['openid']

    def get_account(self, port: str) -> dict:
        """获取小程序账号信息,AppID/AppSecret"""
        return config.WECHAT_ACCOUNTS[port]


def get_access_token(self) -> str:
    """优先从redis缓存中获取"""
    access_token = self.Redis.get(self.access_token_redis_key)
    if access_token:
        return access_token
    else:
        return self.update_access_token()


def update_access_token(self) -> str:
    """向腾讯服务器请求"""
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={config.APP_ID}&secret={config.APP_SECRET}'

    result = requests.get(url=url)
    result = result.json()
    access_token = result['access_token']
    self.Redis.set(self.access_token_redis_key, access_token, ex=7140)
    return access_token


def __call__(self, *args, **kwargs):
    from init import Redis
    self.Redis = Redis
