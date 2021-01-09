"""
__author__ = 'jaxon'
__time__ = '2021/1/9 下午3:04'
__desc__ = ''
"""

# 启动app、关闭app、重启app、进入首页
from appium import webdriver

from appium_test.page.base_page import BasePage
from appium_test.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # 不清空缓存启动app
            caps["noReset"] = "true"
            # 设置等待页面空闲状态的时间为0s
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 显式等待10s
            self.driver.implicitly_wait(10)
        else:
            # 根据caps内设置的app信息启动app
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
