#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 21:10
# @Author   : ZhangTao
# @File     : del_contact_page.py
from appium.webdriver.common.mobileby import MobileBy
from assignments.appium_practice.second_practice.page.base_page import BasePage


class DelContactPage(BasePage):
    def del_contact(self):
        # 点击删除成员
        self.find(MobileBy.XPATH, '//*[@text="删除成员"]').click()

        # 点击确定
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()