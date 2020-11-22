#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 17:27
# @Author   : ZhangTao
# @File     : test_search.py
from practices.appium_pra.framework.page.app_page import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search('jd')