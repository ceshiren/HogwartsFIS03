"""
__author__ = 'jaxon'
__time__ = '2021/1/9 下午4:10'
__desc__ = ''
"""
# find、find_and_clcik、滚动查找等
# from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element(*locator)

    def find_and_click(self,locator):
        self.find(locator).click()

    def find_by_scroll_and_click(self,text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));')
        self.find_and_click(ele)

    def find_and_get_text(self, locator):
        return self.find(locator).text