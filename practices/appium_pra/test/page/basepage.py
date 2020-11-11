#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 21:00
# @Author   : ZhangTao
# @File     : basepage.py
import yaml
from appium.webdriver.webdriver import WebDriver
from typing import List
from selenium.webdriver.common.by import By


class BasePage:
    # 定义弹窗黑名单
    _black_list = [(By.ID, "image_cancel")]
    # 设置错误计数器
    _error_count = 0
    # 设置最大错误数
    _error_max = 10
    _params = {}

    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    # 定义查找元素方法
    def find(self, by, locator=None):
        try:
            # 利用三目运算符定义
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_count = 0

        # 弹窗处理
        except Exception as e:
            # 计数器每循环一次加一
            self._error_count += 1
            # 如果计数器值大于最大错误数，则跑出异常
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                # 将弹窗元素赋予elements
                elements = self._driver.find_elements(*black)
                # 如果弹窗元素存在则点击第一个弹窗
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            # 计数器每循环一次加一
            self._error_count += 1
            # 如果计数器值大于最大错误数，则跑出异常
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                # 将弹窗元素赋予elements
                elements = self._driver.find_elements(*black)
                # 如果弹窗元素存在则点击第一个弹窗
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e

    # 定义读取外部文件方法
    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # 指明steps的类型:列表中套用字典
            steps: List[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" in step.keys():
                        # {value}
                        content:str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}"%param, self._params[param])
                        self.send(content, step["by"], step["locator"])

