"""
__author__ = 'jaxon'
__time__ = '2020/12/19 下午3:31'
__desc__ = ''
"""
import pytest

from selenium_web.selenium_po.page.main_page import MainPage


class TestLogin:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,mail", [("wangwu1", "wangwu1", "wangwu1@qq.cm")])
    def test_login(self, name, id, mail):
        # name = "zhangsan"
        # id = "asdfas1"
        # mail = "asdqweq@qq.com"
        namelist = self.main.goto_contact_page().click_add_member(). \
            add_memebr(name, id, mail).get_member()
        print(namelist)
        assert name in namelist
