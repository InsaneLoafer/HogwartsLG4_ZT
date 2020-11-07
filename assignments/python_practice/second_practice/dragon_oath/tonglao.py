#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 11:10
# @Author   : ZhangTao
# @File     : tonglao.py

"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，
如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“师弟是我的！”，
如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），
调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。
血多的一方获胜。
"""

# 定义天山童姥类
class TongLao:
    # 构造方法定义血量和武力值
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    # 定义see_people 方法
    def see_people(self, name):
        # 如果传入”WYZ”（无崖子），则打印，“师弟！！！！”
        if name == "WYZ":
            print("师弟！！！")

        # 如果传入“李秋水”，打印“师弟是我的！”
        elif name == "LQS":
            print("师弟是我的！")

        # 如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif name == "DCQ":
            print("叛徒！我杀了你！")

    # 定义fight_zms（天山折梅手)方法，传入敌人的血量和武力值
    def fight_zms(self, enemy_hp, enemy_power):
        # 童姥武力值提升10倍
        self.power *= 10
        # 童姥血量缩减2倍
        self.hp /= 2
        # 进行pk
        self.hp -= enemy_power
        enemy_hp -= self.power
        # 判断最终血量
        # 如果童姥血量比敌人血量高，童姥胜利
        if self.hp > enemy_hp:
            # 空一行
            print()
            print(f"<<<<<------童姥血量:敌人血量={self.hp}:{enemy_hp}------>>>>>")
            # 空一行
            print()
            print("哈哈哈！你终究还是敌不过我的天山折梅手！")
        # 如果童姥血量小等于敌人血量高，童姥失败
        elif self.hp <= enemy_hp:
            # 空一行
            print()
            print(f"<<<<<------童姥血量:敌人血量={self.hp}:{enemy_hp}------>>>>>")
            # 空一行
            print()
            print("你...你...居然敌得过我的天山折梅手！啊~~~")

# 将类实例化
if __name__ == "__main__":

    # 赋予童姥血量1000，武力值10
    tonglao = TongLao(1000, 10)

    # 调用see_people函数
    tonglao.see_people("WYZ") # 结果为：师弟！！！
    tonglao.see_people("LQS") # 结果为：师弟是我的！
    tonglao.see_people("DCQ") # 结果为：叛徒！我杀了你！

    # 调用天山折梅手函数
    # 敌人血量2000，武力值50，童姥战败的情况
    tonglao.fight_zms(2000, 50)
    # 敌人血量500，武力值50，童姥胜利的情况
    tonglao.fight_zms(500, 50)


