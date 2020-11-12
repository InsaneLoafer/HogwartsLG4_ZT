#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 14:02
# @Author   : ZhangTao
# @File     : app.py
import yaml
from appium import webdriver
from practices.appium_pra.demo.page.basepage import BasePage
from practices.appium_pra.demo.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["autoGrantPermission"] = True
            caps["udid"] = yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(5)
        return self

    def main(self) -> Main:
        return Main(self._driver)