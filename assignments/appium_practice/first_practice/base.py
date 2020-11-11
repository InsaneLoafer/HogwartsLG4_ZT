#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 10:07
# @Author   : ZhangTao
# @File     : base.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Base:
    nameList = ["aa11", "aa22"]

    def caps(self):
        desire_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": 'true',
            "skipDeviceInitialization": 'true',
            "skipServerInstallation": 'true',
            # "dontStopAppOnReset": True,
            "unicodeKeyBoard": 'true', # 设置后可输入中文
            "resetKeyBoard": 'true' # 重置键盘
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(5)


    def fXpath(self, locator):
        return self.driver.find_element(MobileBy.XPATH, locator)

    def fXpaths(self, locator):
        return self.driver.find_elements(MobileBy.XPATH, locator)

    # 定义打开通讯录方法
    def open_contact(self):
        return self.fXpath('//*[@text="通讯录"]').click()

    # 定义滚动查找并点击操作
    def scroll_find(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{text}").instance(0));').click()



