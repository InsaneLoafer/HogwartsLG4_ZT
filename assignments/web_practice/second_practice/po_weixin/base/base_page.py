#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/7 22:37
# @Author   : ZhangTao
# @File     : base_page.py
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _base_url = ""
    # 是否复用浏览器参数
    _dul_chrome = ""

    # 可复用之前的driver，避免执行一个页面或用例后就关闭浏览器
    def __init__(self, driver:WebDriver=None):
        self._driver = ""
        if driver == None:
            if self._dul_chrome == "yes":
                option = Options()
                option.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=option)

            else:
                self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        # 如果url不为空，则初始化页面
        if self._base_url != "":
            self._driver.implicitly_wait(5)
            self._driver.maximize_window()
            self._driver.get(self._base_url)


    # 定义find方法
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    # 同上
    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 定义显示等待元素出现方法
    def wait_for_click(self, locator, timeout=10):
        WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

