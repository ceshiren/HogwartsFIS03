"""
__author__ = 'jaxon'
__time__ = '2021/1/9 下午3:15'
__desc__ = ''
"""
# 测试用例
import pytest
import yaml

from appium_test.page.app import App

def get_data():
    with open("../data/data.yaml", encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        addnumber = data["add"]
        return addnumber

class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    # @pytest.mark.parametrize("name,gender,phonenum",(
    #         ["wangwu1","女","18300000001"],
    #         ["wangwu2", "男", "18300000002"]
    # ))
    @pytest.mark.parametrize("name,gender,phonenum",get_data())
    def test_add_contact(self,name,gender,phonenum):
        # name = "wangwu"
        # gender = "女"
        # phonenum = "18300000000"
        toast = self.main.click_addresslist().add_member().addconect_menual(). \
            edit_name(name).edit_gender(gender).edit_phone(phonenum).cilck_save().get_toast()
        assert toast == "添加成功"
