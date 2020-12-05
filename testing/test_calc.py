# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_calc.py
import allure
import pytest
import yaml

from python_code.calc import Calculator




@allure.feature("测试计算器")
class TestCalc:

    # def setup_class(self):
    #     print("开始计算")
    #     # 实例化计算器类
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # @pytest.mark.parametrize(
    #     "a, b, expect",
    #     add_datas, ids=myid
    # )
    @pytest.mark.add
    @allure.story("测试加法")
    def test_add(self,get_calc, get_add_datas):
        result = None
        try:
            # 实例化计算器类
            # calc = Calculator()
            # 调用 add 方法
            with allure.step("计算两个数的相加和"):
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            # 判断 result 是浮点数，作出保留2为小数的处理
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        # 得到结果之后，需要写断言
        assert result == get_add_datas[2]

    @pytest.mark.add
    def test_add2(self, get_calc):
        result = get_calc.add(0.1, 0.2)
        assert round(result, 2) == 0.3

    @pytest.mark.div
    def test_div(self):
        print("test_div")

    @pytest.mark.sub
    def test_sub(self):
        print("test_sub")

    @pytest.mark.mul
    def test_mul(self):
        print("test_mul")

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
