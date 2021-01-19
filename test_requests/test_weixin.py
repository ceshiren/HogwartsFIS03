import requests


class TestWeiXin:
    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "ww93348658d7c66ef4", "corpsecret": "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"}
        r = requests.request(method="GET", url=url, params=params)
        self.token = r.json()["access_token"]
        assert r.json()["errcode"] == 0

    def test_create_department(self):

        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {
            "name": "广州研发中心2",
            "name_en": "RDGZ2",
            "parentid": 1,
            "order": 1,
            "id": 3}
        params = {
            "access_token":self.token
        }

        r = requests.request(method="POST", url=url, params = params,json=data)
        assert r.json()["errcode"] == 0

    def test_update_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/" \
              f"department/update?access_token={self.token}"
        data = {
            "name": "广州研发中心无限2",
            "name_en": "RDGZ2",
            "parentid": 1,
            "order": 1,
            "id": 3
        }
        r = requests.request(method="POST", url=url, json = data)
        assert r.json()["errmsg"] == "updated"

    def test_delete_department(self):
        id = 3
        # 字面量插值
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}"
        r = requests.request(method="GET", url = url)
        assert r.json()["errmsg"] == "deleted"

    def test_get_list(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.request(method="GET", url = url)
        print(r.json())

    def test_demo(self):
        name = "lisa"
        print(f"My name is {name}, my age is 16")