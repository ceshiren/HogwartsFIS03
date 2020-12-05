# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_demo1.py
import pytest


@pytest.fixture()
def connectDB():
    print("test_demo1 下面的 connectDB 方法")


def test_a(connectDB):
    print(" sub_demo test_a")


def test_b(connectDB):
    print("sub_demo test_b")