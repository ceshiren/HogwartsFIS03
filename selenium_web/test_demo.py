"""
__author__ = 'jaxon'
__time__ = '2020/12/19 下午2:26'
__desc__ = ''
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_contacts").click()
    ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    # 显示等待，等待元素是可点击状态
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(ele))
    # 解决点击无效问题；设置死循环多次点击，直到目标元素出现后，跳出死循环
    while True:
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id("username")
        if len(element) > 0:
            break
    driver.find_element_by_id("username").send_keys("5151155")
    driver.find_element_by_id("memberAdd_acctid").send_keys("xx151utuds")
    driver.find_element_by_id("memberAdd_mail").send_keys("s1sa51t1d@qq.com")
    driver.find_element_by_css_selector(".js_btn_save").click()
    time.sleep(1)
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    name_list = []
    for value in eles:
        # 获取元素属性title的值，存入list内
        print(value.get_attribute("title"))
        name_list.append(value.get_attribute("title"))
    # 断言目标名字是否在列表内
    assert "5151155" in name_list
    print(name_list)