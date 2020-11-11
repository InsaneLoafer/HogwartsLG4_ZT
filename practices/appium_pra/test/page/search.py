#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 21:54
# @Author   : ZhangTao
# @File     : search.py
from practices.appium_pra.test.page.basepage import BasePage


class Search(BasePage):
    def search(self, value):
        self._params["value"] = value
        self.steps("../page/search.yaml")
