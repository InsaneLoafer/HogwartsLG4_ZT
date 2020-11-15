#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 13:33
# @Author   : ZhangTao
# @File     : app.py
"""
app.py 用于启动、关闭、重启、进入主页等操作
"""
from assignments.appium_practice.second_practice.page.base_page import BasePage
from assignments.appium_practice.second_practice.page.main_page import MainPage
from appium import webdriver


class App(BasePage):
    def start(self):
        # 如果driver没有定义，则进行初始化
        if self.driver == None:
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
        # 否则就继承之前的driver
        else:
            # 启动app, 启动的页面是desirecaps里面设置的activity
            self.driver.launch_app()

        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)