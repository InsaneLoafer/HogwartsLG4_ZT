#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/9 14:59
# @Author   : ZhangTao
# @File     : demo1.py
from appium import webdriver

desire_caps = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.nsfocus.adbos.cloudapp",
  "appActivity": ".MainActivity",
    "noReset": False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                   "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                   "android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                   "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                   "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                   "android.view.ViewGroup[4]")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/"
                                   "android.widget.LinearLayout/android.widget.FrameLayout/"
                                   "android.widget.LinearLayout/android.widget.FrameLayout/"
                                   "android.widget.FrameLayout/android.view.ViewGroup/"
                                   "android.view.ViewGroup/android.view.ViewGroup/"
                                   "android.view.ViewGroup/android.view.ViewGroup/"
                                   "android.view.ViewGroup/android.view.ViewGroup/"
                                   "android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
el2.send_keys("https://10.66.250.231")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                   "android.widget.FrameLayout/android.widget.LinearLayout/"
                                   "android.widget.FrameLayout/android.widget.FrameLayout/"
                                   "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                   "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                   "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]")
el3.click()

el11 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                    "android.widget.FrameLayout/android.widget.LinearLayout/"
                                    "android.widget.FrameLayout/android.widget.FrameLayout/"
                                    "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                    "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/"
                                    "android.view.ViewGroup[1]/android.widget.EditText")
el11.send_keys("admin")
el22 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                    "android.widget.FrameLayout/android.widget.LinearLayout/"
                                    "android.widget.FrameLayout/android.widget.FrameLayout/"
                                    "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                    "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/"
                                    "android.view.ViewGroup[2]/android.widget.EditText")
el22.send_keys("xinchuan@123")
el33 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                    "android.widget.FrameLayout/android.widget.LinearLayout/"
                                    "android.widget.FrameLayout/android.widget.FrameLayout/"
                                    "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                    "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]")
el33.click()

