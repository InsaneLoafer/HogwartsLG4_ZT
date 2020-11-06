#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/5 22:23
# @Author   : ZhangTao
# @File     : test_form.py
from time import sleep
from selenium import webdriver

class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.find_element_by_id('user_login').send_keys('123')
        self.driver.find_element_by_id('user_password').send_keys('password')
        self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_xpath('//*[@name="commit"]').click()
        sleep(5)
