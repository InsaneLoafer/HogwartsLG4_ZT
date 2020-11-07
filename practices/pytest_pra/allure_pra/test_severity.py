#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/5 9:43
# @Author   : ZhangTao
# @File     : test_severity.py

"""
按照用例重要级别执行：
@allure.severity(allure.severity_level.TRIVIAL)

执行时：
pytest -s -v 文件名 --allure-severities normal,critical

Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
Critical级别：临界缺陷（功能点缺失）
Normal级别：普通缺陷（数值计算错误)
Minor级别：次要缺陷（界面错误与UI需求不符）
Trivial级别：轻微缺陷（必输项无提示，或提示不规范）
"""

import allure

@allure.severity(allure.severity_level.BLOCKER)
def test_with_block_severity():
    pass

@allure.severity(allure.severity_level.CRITICAL)
def test_with_critical_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_calss_with_overrding_critical_severity(self):
        pass