#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 14:11
# @Author   : ZhangTao
# @File     : test_main.py
import pytest
import yaml
from practices.appium_pra.demo.testcase.test_base import TestBase


class TestMain(TestBase):
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./test_main.yaml")))
    def test_main(self, value1, value2):
        self.app.start().main().goto_search()
        print(value1)
        print(value2)

    def test_window(self):
        self.app.start().main().goto_window()