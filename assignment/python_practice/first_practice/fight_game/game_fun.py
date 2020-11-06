#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/10/21 10:52
# @Author   : ZhangTao
# @File     : game_fun.py

import random

def game_fight(enemy_hp, enemy_power):
    # 定义4个变量，分别为玩家血量/攻击力，敌人血量/攻击力
    my_hp = 1000
    my_power = 200

    # 打印敌人的血量及攻击力
    print(f'敌人的血量为{enemy_hp}，敌人的攻击力为{enemy_power}')

    # 定义最终血量的计算方式
    while True:
        my_hp  -= enemy_power
        enemy_hp -= my_power
        print(my_hp)

        #判断输赢
        if my_hp <= 0:
            print(f"我的血量是{my_hp}:敌人血量{enemy_hp}我输了！")
            break
        elif enemy_hp <= 0:
            print(f"我的血量{my_hp}:敌人血量{enemy_hp}我赢了")
            break

if __name__ == '__main__':
    # 利用列表推导式生成血量
    hp = [x for x in range(910, 1001)]
    # print(hp, type(hp)) #打印hp及其类型

    #让敌人从hp列表中随机选取一个血量
    enemy_hp = random.choice(hp)

    #随机生成敌人的攻击力
    enemy_power = random.randint(100,201)

    #调用函数
    game_fight(enemy_hp, enemy_power)