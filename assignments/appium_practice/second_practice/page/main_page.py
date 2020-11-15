#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 13:35
# @Author   : ZhangTao
# @File     : main_page.py

# 主页
from appium.webdriver.common.mobileby import MobileBy

from assignments.appium_practice.second_practice.page.base_page import BasePage
from assignments.appium_practice.second_practice.page.contact_list_page import ContactListPage


class MainPage(BasePage):
    def goto_contaclist(self):
        """
        进入到通讯录页面
        :return:
        """
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return ContactListPage(self.driver)