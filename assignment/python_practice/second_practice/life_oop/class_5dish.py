#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/24 23:22
# @Author   : ZhangTao
# @File     : class_5dish.py

"""
描述川菜类：
1、火锅，麻辣
2、回锅肉，飘香
3、钵钵鸡，回味无穷
"""
# 定义川菜类
class SichuanDishes:
    # 构造方法，定义名称特色类型
    def __init__(self, name, feature):
        self.name = name
        self.feature = feature

    # 定义类方法，打印各种川菜的特性
    def dish_feature(self):
        print(f"该川菜是{self.name}，特色是{self.feature}。")

# 将类实例化
if __name__ == "__main__":
    hotpot = SichuanDishes("火锅", "麻辣")
    huiguorou = SichuanDishes("回锅肉", "飘香")
    boboji = SichuanDishes("钵钵鸡", "回味无穷")
    # 调用类方法
    hotpot.dish_feature()
    huiguorou.dish_feature()
    boboji.dish_feature()
