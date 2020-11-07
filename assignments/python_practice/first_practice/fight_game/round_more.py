#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/21 10:41
# @Author   : ZhangTao
# @File     : round_more.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

def game_fight():
    # 定义4个变量，分别为玩家血量/攻击力，敌人血量/攻击力
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 定义最终血量的计算方式
    while True:
        my_hp  -= enemy_power
        enemy_hp -= my_power
        print(my_hp)

        #判断输赢
        if my_hp <= 0:
            print(f"我的血量{my_hp}:敌人血量{enemy_hp}我输了！")
            break
        elif enemy_hp <= 0:
            print(f"我的血量{my_hp}:敌人血量{enemy_hp}我赢了")
            break

if __name__ == '__main__':
    game_fight()
