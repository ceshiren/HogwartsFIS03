
from test_requests.test_weixin.wework import WeWork


class Department(WeWork):
    def create_department(self, name, name_en, department_id):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "json": {"name": name, "name_en": name_en, "parentid": 1, "order": 1, "id": department_id},
            "params": {"access_token": self.token},
            "method": "post"
        }
        r = self.send(req)
        return r.json()

    def update_department(self, name):
        # 字典的key值，一定要和request对应要求的key值是一致的
        req = {"url": f"https://qyapi.weixin.qq.com/cgi-bin/" \
                      f"department/update?access_token={self.token}",
               "json": {"name": name, "id": 4},
               "method": "post"
               }
        r = self.send(req)
        return r.json()

    def delete_department(self, department_id):
        # 字面量插值
        # 使用字典保存url以及method的信息，即接口的请求信息
        req = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}",
            "method": "get"}
        r = self.send(req)
        return r.json()

    def get_department_list(self):
        req = {"url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}",
               "method": "get"}
        r = self.send(req)
        return r.json()
