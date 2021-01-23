import requests
from jsonpath import jsonpath


class BaseApi:

    def send(self, req):
        """
        :param req: 接口的请求信息 type： dict
        :return:
        """
        # ctrl+鼠标左键，即可点击查看api的使用
        # 1. 使用字典保存url以及method的信息，即接口的请求信息
        # 2. 调用send函数，传入这个字典信息
        ## 两个**代表解包字典， 然后以关键字传参的方式传入参数信息
        ## 3. req 即为传入的字典
        ## 4. **req解包字典，然后以关键字传参的方式传入参数信息
        # req = {
        #     "url" : f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}",
        #     "method": "get"
        # }
        # 5. req解包前是一个字典， 解包后，即为 url = xxx, method = "get"
        # 解包后， return requests.request(**req) 就等于
        # return requests.request(url = xxx, method = "get")
        return requests.request(**req)

    def jsonpath_res(self, obj, expr):
        return jsonpath(obj, expr)

