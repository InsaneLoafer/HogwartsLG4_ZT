#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 9:57
# @Author   : ZhangTao
# @File     : base.py
from selenium import webdriver
import os

class Base():
    def setup(self):
        """
        多浏览器操作
        命令行加上 browser=浏览器名 pytest 文件名
        :return:
        """
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()

        elif browser == 'headless':
            self.driver = webdriver.PhantomJS

        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()