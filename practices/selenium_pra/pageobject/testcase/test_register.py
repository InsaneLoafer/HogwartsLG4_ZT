#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 18:06
# @Author   : ZhangTao
# @File     : test_register.py
from practices.selenium_pra.pageobject.page.main import Main

class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register() # 断言在首页直接进行注册

    def test_login_regiter(self):
        assert self.main.goto_login().goto_register().register() # 断言先进入登录界面，再进行注册

    def teardown(self):
        pass
