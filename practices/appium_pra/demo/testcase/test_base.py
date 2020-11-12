#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 16:19
# @Author   : ZhangTao
# @File     : test_base.py
from practices.appium_pra.demo.page.app import App


class TestBase:
    app = None
    def setup(self):
        self.app = App()
