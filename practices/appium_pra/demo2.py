#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/9 21:23
# @Author   : ZhangTao
# @File     : demo2.py
from appium import webdriver

desire_caps = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
  "appActivity": ".common.MainActivity",
    "noReset": False,
    "skipDeviceInitialization": True,
    "dontStopAppOnReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
driver.implicitly_wait(5)
driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
#                              'android.widget.LinearLayout/android.widget.FrameLayout/'
#                              'android.view.ViewGroup/android.widget.FrameLayout/'
#                              'android.widget.LinearLayout/android.widget.RelativeLayout/'
#                              'android.widget.FrameLayout/android.widget.LinearLayout/'
#                              'androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/'
#                              'android.widget.LinearLayout/android.widget.TextView[1]').click()

