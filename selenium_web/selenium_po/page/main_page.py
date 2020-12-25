"""
__author__ = 'jaxon'
__time__ = '2020/12/19 下午3:21'
__desc__ = ''
"""
from selenium.webdriver.common.by import By

from selenium_web.selenium_po.page.basepage import BasePage
from selenium_web.selenium_po.page.contact_page import ContactPage


# 首页
class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact_page(self):
        self.find(By.ID, "menu_contacts").click()

        return ContactPage(self.driver)
