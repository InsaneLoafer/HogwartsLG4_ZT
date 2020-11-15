#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 21:07
# @Author   : ZhangTao
# @File     : contact_setting_page.py
from appium.webdriver.common.mobileby import MobileBy
from assignments.appium_practice.second_practice.page.base_page import BasePage
from assignments.appium_practice.second_practice.page.del_contact_page import DelContactPage


class ContactSetting(BasePage):
    def goto_contact_edit(self):
        self.find(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return DelContactPage(self.driver)
