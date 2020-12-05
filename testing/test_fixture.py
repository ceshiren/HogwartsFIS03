# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_fixture.py
import pytest

# 创建了登录的 fixture 方法
@pytest.fixture()
def login():
    print("登录操作")
    username = "feier"
    password = "123456"
    token = "token123456"
    yield [username, password, token]
    print("登出操作")


# 测试用例1：需要提前登录
def test_case1(connectDB):
    print(f"login information:{login}")
    print("测试用例1")

def test_case2():
    print("测试用例2")

# 测试用例3：需要提前登录
def test_case3():
    print("测试用例3")

# 测试用例4：需要提前登录
# @pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")