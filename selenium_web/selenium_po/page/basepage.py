"""
__author__ = 'jaxon'
__time__ = '2020/12/19 下午4:14'
__desc__ = ''
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver_base = ""

    def __init__(self, _driver_base: WebDriver = None):
        # 避免driver重复初始化，第一次初始化的时候，driver是空的，所以走到了
        # if的逻辑
        if _driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = _driver_base

        if self._driver_base != "":
            self.driver.get(self._driver_base)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        element: WebDriver = WebDriverWait(self.driver, timeout).until \
            (expected_conditions.element_to_be_clickable(locator))
        return element
