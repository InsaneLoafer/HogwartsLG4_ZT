#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/3 12:50
# @Author   : ZhangTao
# @File     : test_wait.py

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()
        # def wait(x):
        #     return len(self.driver.find_element(By.XPATH, '//*[@class="table-heading"]')) >=1
        #
        # WebDriverWait(self.driver, 10).until(wait) # wait函数传参不能加括号
        # self.driver.find_elements(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))