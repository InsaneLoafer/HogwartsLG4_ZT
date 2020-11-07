#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 17:35
# @Author   : ZhangTao
# @File     : main.py
from selenium.webdriver.common.by import By
from practices.selenium_pra.pageobject.page.base_page import BasePage
from practices.selenium_pra.pageobject.page.login import Login
from practices.selenium_pra.pageobject.page.register import Register


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/'
    def goto_register(self):
        self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)
