#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 20:30
# @Author   : ZhangTao
# @File     : test_register.py
import allure
import pytest
from assignments.web_practice.second_practice.po_weixin.pages.main_page import MainPage

@allure.feature('测试注册功能')
class TestRegiter:
    company_name = '霍格沃兹'
    manager_name = 'michael'
    register_tel = '13311111111'

    def setup(self):
        self.main = MainPage()

    @allure.story('测试直接从主页面进入注册页进行注册')
    def test_main2regiter(self):
        assert self.main.goto_register().register(
            self.company_name, self.manager_name, self.register_tel)

    @allure.story('测试从登录页进入注册页进行注册')
    def test_login2register(self):
        assert self.main.goto_loginpage().goto_register().register(
            self.company_name, self.manager_name, self.register_tel)

if __name__ == '__main__':
    pytest.main('-v', 'test_register.py')


