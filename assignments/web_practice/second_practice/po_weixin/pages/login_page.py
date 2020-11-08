#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 19:13
# @Author   : ZhangTao
# @File     : login_page.py
from selenium.webdriver.common.by import By
from assignments.web_practice.second_practice.po_weixin.base.base_page import BasePage
from assignments.web_practice.second_practice.po_weixin.pages.index_pages.index_page import IndexPage
from assignments.web_practice.second_practice.po_weixin.pages.register_page import RegisterPage
from time import sleep

class LoginPage(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.LINK_TEXT, '企业注册').click()
        return RegisterPage(self._driver)
