#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 21:36
# @Author   : ZhangTao
# @File     : app.py
from appium import webdriver
from practices.appium_pra.test.page.basepage import BasePage
from practices.appium_pra.test.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermission"] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)