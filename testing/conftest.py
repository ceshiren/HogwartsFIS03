# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : conftest.py
from typing import List

import pytest
import yaml
import os
from python_code.calc import Calculator

# 获取 yaml 文件所在的绝对路径
yaml_file_path = os.path.dirname(__file__) + "/datas/calc.yaml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)

@pytest.fixture(params=add_datas, ids=myid)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(scope='session')
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")


@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    print("items")
    print(items)
    # 实现用例反转执行
    items.reverse()

    # 修改测试用例参数编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # item.nodeid 拿到的是测试用例的名称
        # 自动给测试用例加上标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
