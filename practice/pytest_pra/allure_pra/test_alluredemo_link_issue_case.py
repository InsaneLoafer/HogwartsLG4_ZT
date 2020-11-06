#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/2 22:11
# @Author   : ZhangTao
# @File     : test_alluredemo_link_issue_case.py
import allure

@allure.link("http://www.baidu.com", name="连接") # 为该链接添加名字
def test_with_link():
    print("这是一条加了连接的测试")
    pass

"""
运行时添加
--allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
issue第一个数字为bugid，第二个为bug名称，命令中的{}用于存放bugid
"""
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass