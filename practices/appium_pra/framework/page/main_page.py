#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 17:16
# @Author   : ZhangTao
# @File     : main_page.py
from practices.appium_pra.framework.page.base_page import BasePage
from practices.appium_pra.framework.page.market_page import Market


class Main(BasePage):
    def goto_market(self):
        self.steps('../page/main.yaml')
        return Market(self._driver)