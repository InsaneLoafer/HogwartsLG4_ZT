#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 21:52
# @Author   : ZhangTao
# @File     : market.py
from practices.appium_pra.test.page.basepage import BasePage
from practices.appium_pra.test.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)
