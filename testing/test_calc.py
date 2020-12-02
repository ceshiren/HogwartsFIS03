# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_calc.py
import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)


def test_a():
    print("测试用例a")


class TestCalc:

    def setup_class(self):
        print("开始计算")
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=myid
    )
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用 add 方法
        result = self.calc.add(a, b)
        # 判断 result 是浮点数，作出保留2为小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect

    def test_add2(self):
        result = self.calc.add(0.1, 0.2)
        assert round(result, 2) == 0.3

    # def test_add1(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用 add 方法
    #     result = self.calc.add(0.1, 0.1)
    #     # 得到结果之后，需要写断言
    #     assert result == 0.2
    #
    # def test_add2(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用 add 方法
    #     result = self.calc.add(-1, -1)
    #     # 得到结果之后，需要写断言
    #     assert result == -2
