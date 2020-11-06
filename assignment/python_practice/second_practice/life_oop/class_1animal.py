#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/24 21:50
# @Author   : ZhangTao
# @File     : class_1animal.py

"""
描述动物类：
1、老虎要吃肉，是肉食动物
2、羊吃草，是素食动物
3、哈士奇啥都吃，是杂食动物
"""
# 定义动物类
class Animal:

    # 每个动物都有初始重量、毛色和食物，定义类变量
    weight = 100
    color = "white"
    food = "grass"

    # 用构造方法定义传入每种动物名称
    def __init__(self, animal_name):
        self.animal_name = animal_name

    # 打印每种动物的食性、重量和毛色，定义类方法
    def nature(self):
        # 如果是老虎，则吃肉，体重150kg，颜色为黄白色
        if self.animal_name == "tiger":
            self.food = "肉"
            self.weight = 150
            self.color = "黄白相间"

        # 如果是羊，则吃草，体重120kg，毛色为白色
        elif self.animal_name == "sheep":
            self.food = "草"
            self.weight = 120
            self.color = "白"

        # 如果是哈士奇，则啥都吃，体重100kg，毛色为黑白色
        elif self.animal_name == "husky":
            self.food = "任何东西"
            self.weight = 100
            self.color = "黑白"

        # 最后打印每种动物的属性
        print(f"我是{self.animal_name},我最爱吃{self.food}，我有{self.weight}公斤，我的毛是{self.color}色的。")

# 赋予实例，传参
if __name__ == "__main__":
    # tiger
    tiger = Animal("tiger")
    tiger.nature()

    # sheep
    sheep = Animal("sheep")
    sheep.nature()

    # husky
    husky = Animal("husky")
    husky.nature()
