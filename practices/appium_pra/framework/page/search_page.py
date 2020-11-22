#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 17:22
# @Author   : ZhangTao
# @File     : search_page.py
from practices.appium_pra.framework.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._params['value'] = value
        self.steps('../page/search.yaml')