#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 21:48
# @Author   : ZhangTao
# @File     : main.py
from practices.appium_pra.test.page.basepage import BasePage
from practices.appium_pra.test.page.market import Market


class Main(BasePage):
    # 进入行情页
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)