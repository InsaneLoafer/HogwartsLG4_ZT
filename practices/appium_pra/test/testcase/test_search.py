#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 22:00
# @Author   : ZhangTao
# @File     : test_main.py
from practices.appium_pra.test.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")
