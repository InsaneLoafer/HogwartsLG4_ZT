#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 17:19
# @Author   : ZhangTao
# @File     : market_page.py
from practices.appium_pra.framework.page.base_page import BasePage
from practices.appium_pra.framework.page.search_page import Search


class Market(BasePage):
    def goto_search(self):
        self.steps('../page/market.yaml')
        return Search(self._driver)
