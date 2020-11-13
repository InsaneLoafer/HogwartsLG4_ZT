#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 17:37
# @Author   : ZhangTao
# @File     : base.py
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    _base_url = ""

    def __init__(self, driver: WebDriver=None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)