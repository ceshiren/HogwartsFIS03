import requests

from test_requests.test_weixin.base_api import BaseApi


class WeWork(BaseApi):
    """
    用来存放业务的公共步骤，比如获取token
    """
    def __init__(self, secret):
        # 创建一个类变量， 通过调用self.get_token()函数，获取到token信息
        self.token = self.get_token(secret)

    def get_token(self, secret):

        req = {"url" : "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        "params" : {"corpid": "ww93348658d7c66ef4", "corpsecret": secret},
        "method": "get"}
        r = self.send(req)
        return r.json()["access_token"]