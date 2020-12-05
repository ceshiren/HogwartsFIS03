# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : conftest.py
import pytest


@pytest.fixture()
def connectDB():
    print("这是 sub_demo 的 connectDB 方法")