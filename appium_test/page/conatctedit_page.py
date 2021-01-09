"""
__author__ = 'jaxon'
__time__ = '2021/1/9 下午3:12'
__desc__ = ''
"""


# 添加成员信息（姓名、性别、邮箱）
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.mobile import Mobile

from appium_test.page.base_page import BasePage


class ConatctEditPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def edit_name(self,name):
        # self.driver.find_element_by_xpath \
        #     ("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("abc5")
        name_element = (MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText")
        self.find(name_element).send_keys(name)
        return self

    def edit_gender(self,gender):
        # gender = "女"
        # self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.find_and_click((MobileBy.XPATH,"//*[@text='男']"))
        if gender == "女":
            self.find_and_click((MobileBy.XPATH,"//*[@text='女']"))
        else:
            self.find_and_click((MobileBy.XPATH,"//*[@text='男']"))
        return self

    def edit_phone(self,phonenum):
        # self.driver.find_element_by_id("com.tencent.wework:id/eq7").send_keys("18900000005")
        self.find((MobileBy.ID,"com.tencent.wework:id/eq7")).send_keys(phonenum)
        return self

    def cilck_save(self):
        # self.driver.find_element_by_id("com.tencent.wework:id/gur").click()
        self.find_and_click((MobileBy.ID,"com.tencent.wework:id/gur"))
        from appium_test.page.memberInvite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
