#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/24 22:22
# @Author   : ZhangTao
# @File     : class_2lol.py
"""
描述英雄联盟人物类：
1、剑圣有高原血统，会说“你的剑就是我的剑”；
2、亚索有龙卷风，会说“哈撒给！”；
3、提莫有蘑菇，会说“我去前方探探路”。
"""
# 定义LOL任务类
class LOLPerson:
    # 类变量，定义人物初始属性
    skill = ""
    motto = ""

    # 构造方法传入人物名称
    def __init__(self, name):
        self.name = name

    # 定义任务属性类方法
    def person_nature(self):
        # 逻辑判断
        if self.name == "剑圣":
            self.skill = "高原血统"
            self.motto = "你的剑就是我的剑"

        elif self.name == "亚索":
            self.skill = "龙卷风"
            self.motto = "哈撒给"

        elif self.name == "提莫":
            self.skill = "蘑菇"
            self.motto = "我去前方探探路"

    # 定义打印方法
    def print_person(self):
        print(f"我是{self.name}，我拥有{self.skill}，我的座右铭是{self.motto}。")

# 定义实例，传参
if __name__ == "__main__":
    # 创建人物名字列表
    person_list = ["剑圣", "亚索", "提莫"]

    # 遍历列表，将类实例化，并调用实例化后的类方法
    for lolname in person_list:
        person_name = LOLPerson(lolname)
        person_name.person_nature()
        person_name.print_person()



