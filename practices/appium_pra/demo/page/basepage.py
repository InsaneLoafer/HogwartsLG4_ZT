#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 14:00
# @Author   : ZhangTao
# @File     : basepage.py
import yaml
from appium.webdriver.webdriver import WebDriver
from typing import List
from selenium.webdriver.common.by import By


class BasePage:
    _driver:WebDriver
    # 定义弹窗黑名单
    _black_list = [(By.ID, 'iv_close')]
    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            for black in self._black_list:
                # 参数列表中的*args代表一个元组参数,适用于在定义函数的时候，并不确定参数究竟需要几个的场景
                # 参数列表中的**args代表一个字典参数，字典中都有确定的键值对
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            # 处理完黑名单后再次找到原来的元素
            return self.find(locator, value)

    def steps(self, path):
        with open(path) as f:
            steps: List[dict] = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in steps:
                action = step["action"]
                if action == "click":
                    element.click()