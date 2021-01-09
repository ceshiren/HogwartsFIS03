"""
__author__ = 'jaxon'
__time__ = '2021/1/9 下午3:10'
__desc__ = ''
"""
# 点击手动输入添加
from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.base_page import BasePage
from appium_test.page.conatctedit_page import ConatctEditPage


class MemberInvitePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def addconect_menual(self):
        # self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmember_element)
        return ConatctEditPage(self.driver)

    def get_toast(self):
        # mytoast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        mytoast = self.find_and_get_text(toast_element)
        return mytoast

