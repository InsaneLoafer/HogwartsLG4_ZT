#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/5 17:31
# @Author   : ZhangTao
# @File     : test_baidudemo.py
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.testcase('http://www.github.com')
@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data):

    with allure.step('打开百度网页'):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.baidu.com')

    with allure.step(f'输入搜索词{test_data}'):
        driver.find_element(By.ID, 'kw').send_keys(test_data)
        time.sleep(2)

    with allure.step('点击搜索'):
        driver.find_element(By.ID, 'su').click()
        time.sleep(2)

    with allure.step('搜索结果截屏'):
        driver.save_screenshot('./result/b.png')
        allure.attach.file('./result/b.png', attachment_type=allure.attachment_type.PNG)

    with allure.step('退出浏览器'):
        driver.quit()