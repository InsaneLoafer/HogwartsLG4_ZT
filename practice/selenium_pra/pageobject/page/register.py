#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 17:51
# @Author   : ZhangTao
# @File     : register.py
from selenium.webdriver.common.by import By
from practice.selenium_pra.pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, 'corp_name').send_keys('hello')
        self.find(By.ID, 'manager_name').send_keys('username')
        return True
