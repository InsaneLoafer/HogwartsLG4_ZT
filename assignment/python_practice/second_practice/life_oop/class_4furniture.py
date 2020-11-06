#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/24 23:16
# @Author   : ZhangTao
# @File     : class_4furniture.py

"""
描述家具类：
1、茶几，放茶水
2、沙发，坐和躺
3、床，睡觉
"""
# 定义家具类
class Furniture:
    # 构造方法，定义名称、用途
    def __init__(self, name, use):
        self.name = name
        self.use = use

    # 定义类方法，打印各种家具的用途
    def furniture_use(self):
        print(f"该家具是{self.name}，用来{self.use}。")

# 将类实例化
if __name__ == "__main__":
    teapoy = Furniture("茶几", "放茶水")
    sofa = Furniture("沙发", "坐和躺")
    bed = Furniture("床", "睡觉")
    # 调用类方法
    teapoy.furniture_use()
    sofa.furniture_use()
    bed.furniture_use()
