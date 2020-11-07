#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/2 21:55
# @Author   : ZhangTao
# @File     : test_feature_story.py

"""
运行指定feature的用例：
    pytest 文件名 --allure-features "feature名"

运行指定story的用例
    pytest 文件名 --allure-story "stories名"


"""
import pytest
import allure
@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录： 测试用例 ， 登陆成功")
        pass

    @allure.story("登录失败")
    def test_login_failed(self):
        print("这是登录： 测试用例 ， 登陆失败")
        pass

    @allure.story("用户名缺失")
    def test_login_no_username(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_no_password(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录后登录失败"):
            assert "1" == 1
            print("登录失败")


if __name__ == '__main__':
    pytest.main(["test_feature_story.py"])
