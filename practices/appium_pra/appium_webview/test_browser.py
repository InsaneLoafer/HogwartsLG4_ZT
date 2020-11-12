#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 16:46
# @Author   : ZhangTao
# @File     : test_browser.py
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["platformVersion"] = "6.0"
        caps["browserName"] = "Browser"
        caps["noReset"] = True
        caps["deviceName"] = "hogwarts"
        caps["chromedriverExecutable"] = r"D:\HogwartsLG4_ZT\practices\appium_pra\appium_webview\chromedriver.exe"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
        self.driver.find_element_by_id('index-kw').click()
        self.driver.find_element_by_id('index-kw').send_keys('appium')
        search_locator = (By.ID, 'index-bn')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()