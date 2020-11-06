#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 11:34
# @Author   : ZhangTao
# @File     : xuzhu.py

"""
定义一个XuZhu类，继承于童姥。
虚竹宅心仁厚不想打架。
所以虚竹只有一个read（念经）的方法。
每次调用都会打印“罪过罪过”
"""

# 导入童姥类
from assignment.python_practice.second_practice import TongLao

# 定义XuZhu类
class XuZhu(TongLao):
    # 在构造函数中将童姥的血量设为1000，武力值设为50，传入虚竹的血量和武力值
    def __init__(self, xhp, xpower):
        self.xhp = xhp
        self.xpower = xpower
        super().__init__(1000, 50)

    # 定义read方法
    def read(self):
        print("虚竹说：罪过罪过~")

    """
     定义defense方法，当童姥血量少于敌人的时候，虚竹为童姥报仇
     虚竹不断与敌人交战，且每交战一次虚竹武力值加倍，恢复已损失血量，将敌人击败
    """
    def defense(self, enemy_hp, enemy_power):
        # 调用童姥的天山折梅手
        super().fight_zms(enemy_hp, enemy_power)

        # 判断童姥与敌人血量
        if self.hp <= enemy_hp:
            # 空一行
            print()
            print("狗贼！你居然伤我师傅！看招！！！")
            # 当敌人血量大于0时
            # 定义交战次数
            n = 1
            while enemy_hp > 0:
                # 虚竹与敌人交战
                enemy_hp -= self.xpower
                # 虚竹武力值加倍
                self.power *= 2
                # 交战次数增加
                n += 1

            # 交战完成，打印虚竹此时武力值以及交战次数
            # 空一行
            print()
            print(f"<<<<<-----交战{n}次后----->>>>>")
            # 空一行
            print()
            # 调用一次read方法，说一句“罪过罪过”
            self.read()
            print(f"虚竹说：我终于为师傅报仇啦！你看我武力值都已经{self.power}了，还有谁！！")

# 实例化对象
if __name__ == "__main__":
    # 赋予虚竹血量500，武力值20
    xuzhu = XuZhu(500, 100)
    # 调用defense方法
    xuzhu.defense(1000,50)





