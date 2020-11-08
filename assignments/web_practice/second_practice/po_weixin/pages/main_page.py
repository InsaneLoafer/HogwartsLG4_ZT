#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 19:05
# @Author   : ZhangTao
# @File     : main_page.py
from selenium.webdriver.common.by import By
from assignments.web_practice.second_practice.po_weixin.base.base_page import BasePage
from assignments.web_practice.second_practice.po_weixin.pages.login_page import LoginPage
from assignments.web_practice.second_practice.po_weixin.pages.register_page import RegisterPage


class MainPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/'
    # 定义goto_loginpage方法
    def goto_loginpage(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return LoginPage(self._driver)

    # 定义goto_regiter方法
    def goto_register(self):
        self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self._driver)
