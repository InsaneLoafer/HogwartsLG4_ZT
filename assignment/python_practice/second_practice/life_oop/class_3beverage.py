#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/24 23:04
# @Author   : ZhangTao
# @File     : class_3beverage.py

"""
描述饮料类：
1、可乐，棕黑色，是汽水
2、橙汁，橙色，是水果汁
3、怡宝，无色，是纯净水
"""
# 定义饮料类
class Beverage:
    # 构造方法，定义名称、颜色，饮料类型
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    # 定义类方法，打印各种饮料的属性
    def beverage_nature(self):
        print(f"该饮料是{self.name}，颜色是{self.color}，属于{self.type}类型。")

# 将类实例化
if __name__ == "__main__":
    cola = Beverage("可乐", "棕黑色", "汽水")
    orange_juice = Beverage("橙汁", "橙色", "水果汁")
    yibao = Beverage("怡宝", "无色", "纯净水")
    # 调用类方法
    cola.beverage_nature()
    orange_juice.beverage_nature()
    yibao.beverage_nature()
