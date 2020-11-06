#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 14:37
# @Author   : ZhangTao
# @File     : base.py
from selenium import webdriver

class Base():
    def setup(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
