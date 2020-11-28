#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class 类名:
# 静态属性
# 动态方法

# 属性：姓名，性别，年龄，存款金额....
# 方法：吃，睡，跑....

class Person:
    # 属性：姓名，性别，年龄，存款金额....
    name: str = None
    age: int = 0
    gender: str = "男"
    # 私有属性
    __money: float = 0

    def __get_money(self):
        return self.__money

    def __init__(self, name, age, gender, money):
        print("构造函数")
        self.name = name
        self.age = age
        self.gender = gender
        self.__money = money

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")

    def a(aaa):
        print("aaaa")


class FunnyMan(Person):
    skill: str = ""

    # def __init__(self,skill):
    #     self.skill = skill
    # def __init__(self,skill,name, age, gender, money):
    #     self.skill = skill
    #     super().__init__(name, age, gender, money)

    def fun(self):
        print(f"{self.name} is funny， his skill is {self.skill}")


jl = FunnyMan("搞笑")
print(jl.skill)
print(jl.name)

# st = FunnyMan("单口相声","ST",30,'男',10000)
# print(st.name)
# st.fun()
# st.a()
# print(st)
#
#
# p_ls = Person("李四",20,'男',1000)
# print(p_ls.name)
# print(p_ls.gender)
# print(p_ls.age)
# print(p_ls.__get_money())
# p_ls.run()
#
# print(dir(p_ls))
# print(p_ls._Person__money)

# p_ls = Person()
# print(p_ls.name)
# p_ls.eat()
# p_ls.name = "王五"
# print(p_ls.name)
#
#
# Person.name = "default_name"
# print(Person.name)
# print(p_ls.name)
#
#
#
# p_zl = Person()
# print(p_zl.name)
# # 实例化对象
# p_zs = Person()
# print(p_zs.name)
# p_zs.run()
#
# # 类
# print(Person.name)
# # 不可以通过类直接调用方法
# Person.run()
