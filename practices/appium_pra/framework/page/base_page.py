#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 16:05
# @Author   : ZhangTao
# @File     : base_page.py
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 定义弹窗黑名单
    _black_list = [(By.ID, 'tv_dis_agree')]
    # 定义报错计数器及报错数的最大值
    _error_count = 0
    _error_max = 10
    # 定义变量
    _params = {}
    # 构造函数中定义driver
    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    def find(self, by, locator=None):
        try:
            # 三目运算，避免将by和操作写在一个tuple的行为（By.ID,locator）
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_count = 0
            return element

        except Exception as e:
            # 如果未找到元素报错次数加1
            self._error_count += 1
            # 如果报错计数大于最大值，则直接抛出异常
            if self._error_count >= self._error_max:
                raise e
            # 遍历黑名单列表
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                # 如果有黑名单中有值，则点击第一个弹框
                if len(elements) > 0:
                    elements[0].click()
                    # 最后返回find()函数自身，不断调用
                    return self.find(by, locator)
    def send(self, value, by ,locator):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            # 如果未找到元素报错次数加1
            self._error_count += 1
            # 如果报错计数大于最大值，则直接抛出异常
            if self._error_count >= self._error_max:
                raise e
            # 遍历黑名单列表
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                # 如果有黑名单中有值，则点击第一个弹框
                if len(elements) > 0:
                    elements[0].click()
                    # 最后返回find()函数自身，不断调用
                    return self.send(value, by, locator)

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if 'by' in step:
                    element = self.find(step['by'], step['locator'])
                if 'action' in step.keys():
                    if 'click' == step['action']:
                        element.click()
                    if 'send' == step['action']:
                        content:str = step['value']
                        for param in self._params:
                            content = content.replace("{%s}"%param, self._params[param])
                        self.send(content, step['by'], step['locator'])

