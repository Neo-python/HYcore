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

    def get_open_id(self, code: str) -> str:
        """获取open_id"""
        # if request.get_json(force=True).get('code'):
        #     return request.get_json(force=True).get('code')
        # real_code = request.get_json(force=True).get('code')
        url = f'https://api.weixin.qq.com/sns/jscode2session?appid={self.app_id}&secret={self.app_secret}&js_code={code}&grant_type=authorization_code'
        result = requests.get(url)
        result = result.json()
        return result['openid']

    def get_access_token(self) -> str:
        """优先从redis缓存中获取"""
        access_token = self.Redis.get(self.access_token_redis_key)
        if access_token:
            return access_token
        else:
            return self.update_access_token()

    def update_access_token(self) -> str:
        """向腾讯服务器请求"""
        url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={config.APP_ID}&secret={config.SECRET_KEY}'

        result = requests.get(url=url)
        print(result)

    def __call__(self, *args, **kwargs):
        from init import Redis
        self.Redis = Redis
