#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 11:59
# @Author   : ZhangTao
# @File     : demo.py

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
