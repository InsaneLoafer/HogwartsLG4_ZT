#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 17:09
# @Author   : ZhangTao
# @File     : app_page.py
from appium import webdriver

from practices.appium_pra.framework.page.base_page import BasePage
from practices.appium_pra.framework.page.main_page import Main


class App(BasePage):
    # 定义启动app方法
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = '.view.WelcomeActivityAlias'
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = 'hogwarts'
            caps['appPackage'] = _package
            caps['appActivity'] = _activity
            caps['autoGrantPermission'] = True
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.launch_app()

        return self

    def main(self):
        return Main(self._driver)
