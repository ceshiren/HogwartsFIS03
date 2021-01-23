
import pytest
import yaml

from test_requests.test_weixin.department import Department


class TestWeiXin:
    def setup_class(self):
        # 实例化department类，供测试用例调用
        conf = yaml.load(open("conf.yaml"))
        secret = conf["department_secret"]
        self.department = Department(secret=secret)

    @pytest.mark.parametrize("name,name_en,department_id",
                             [("广州研发中心10", "RDGZ2344", 4),
                              ("广州研发中心111111111111111111111111111111111111111111111111111111111111111111111111111", "RDGZ3", 4)])
    def test_create_department(self, name, name_en, department_id):
        r = self.department.create_department(name, name_en, department_id)
        # 如果名称长度大于32，那么则断言错误码为40058，否则就断言错误码为0
        if len(name)>32:
            assert r["errcode"] == 40058
        else:
            assert r["errcode"] == 0

    @pytest.mark.parametrize("name",["广州研发中心5"])
    def test_update_department(self, name):
        # 更新部门->获取部门列表->获取到部门名称->断言
        r = self.department.update_department(name)
        r2 = self.department.get_department_list()
        name_list = self.department.jsonpath_res(r2, "$..name")
        department_name = self.department.jsonpath_res(r2, "$..department[?(@.id==4)].name")[0]
        assert "广州研发中心5" in name_list
        assert department_name == "广州研发中心5"

    @pytest.mark.parametrize("department_id",[4])
    def test_delete_department(self, department_id):
        r = self.department.delete_department(department_id)
        assert r["errmsg"] == "deleted"


