#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/2 21:35
# @Author   : ZhangTao
# @File     : test_alluredemo1.py
"""
安装：pip install allure-pytest
使用：
    方式一：
    1、运行用例并生成测试报告：
        pytest --alluredir=/tmp/my_allure_results
    2、打开测试报告
        allure serve /tmp/my_allure_results

    方式二：
    1、生成报告：
        allure generate ./result/ -o ./report/ --clean （注意：覆盖路径加上--clean)
    2、打开报告
        allure open -h 127.0.0.1 -p 8883 ./report/ （在本地开启Tomcat服务）
"""

import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')